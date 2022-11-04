from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from reviews.models import User
from .serializers import FullUserSerializer, JWTSerializer, CreateUserSerializer, PatchUserSerializer, CreateUserByAdminSerializer
from reviews.mail import send_letter
from django.shortcuts import get_object_or_404
from reviews.models import get_tokens_for_user
from .permissions import IsAdmin, IsModer, OwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination


@api_view(['POST'])
def create_user(request):
    # проверяем на существование записи в БД по емэйл
    if User.objects.filter(email=request.data.get('email')).exists():
        user = User.objects.get(email=request.data.get('email'))
        # если username из запроса соответсвует записи в базе по емэйл,
        # выбираем сериалайзер без привязки к моделе User.
        # то есть ничего записывать в БД не будем
        if user.username==request.data.get('username'):
            serializer = CreateUserByAdminSerializer(data=request.data)
        else:
            return Response('username не соответствует email', status=status.HTTP_400_BAD_REQUEST)
    else:
        # если email в базе не найден, стандартный сериалайзер
        serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        # проверка на зарезервированное имя 'me'
        if serializer.validated_data['username'] == 'me':
            return Response(
                "Использовать имя 'me' в качестве username запрещено.",
                status=status.HTTP_400_BAD_REQUEST
            )
        # проверяем, какой используется сериалайзер
        # и, при необходимости, записываем в БД
        if isinstance (serializer, CreateUserSerializer):
            serializer.save()
        # переопределяем Юзера
        user = User.objects.get(email=serializer.data['email'])
        conf = user.confirmation_code
        try:
            send_letter(user.email, str(conf), user.username)
            return Response(f'Письмо с кодом подверждения отправлено на {user.email}', status=status.HTTP_200_OK)
        except Exception:
            return Response('Ошибка отправки письма, проверьте адрес почты', status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def send_jwt(request):
    serializer = JWTSerializer(data=request.data)
    if serializer.is_valid():
        # или на .exists() заменить
        try:
            user = User.objects.get(username=serializer.data['username'])
            if str(serializer.data['confirmation_code']) == str(user.confirmation_code):
                return Response(f'token: {get_tokens_for_user(user)}', status=status.HTTP_200_OK)
            else:
                return Response('confirmation_code неверный', status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response('Пользователь не найден', status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PATCH'])
def self_patch_user(request):
    # получаем пользователя по JWT
    user = get_object_or_404(User, id=request.user.id)
    if request.method == 'PATCH':
        serializer = PatchUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = FullUserSerializer(user)
    return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = FullUserSerializer
    permission_classes = (IsAdmin, )
    lookup_field = 'username'
