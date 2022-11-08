from django.core.mail import send_mail  # для тестов
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from reviews.models import get_tokens_for_user, User
from .serializers import FullUserSerializer, JWTSerializer, \
    CreateUserSerializer, PatchUserSerializer, CreateUserByAdminSerializer

from .permissions import IsAdmin    # IsModer, OwnerOrReadOnly


@api_view(['POST'])
def create_user(request):
    """Создаем пользователя по запросу с username и email.
    Возможны 2 варианта: пользователь создается сам впервые,
    и пользователь уже создан админом, необходимо получить JWT."""
    # проверяем на существование записи в БД по емэйл
    if User.objects.filter(email=request.data.get('email')).exists():
        user = User.objects.get(email=request.data.get('email'))
        # если username из запроса соответсвует записи в базе по емэйл,
        # выбираем сериалайзер без привязки к модели User.
        # то есть ничего записывать в БД не будем
        if user.username == request.data.get('username'):
            serializer = CreateUserByAdminSerializer(data=request.data)
        else:
            return Response(
                'username не соответствует email',
                status=status.HTTP_400_BAD_REQUEST
            )
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
        if isinstance(serializer, CreateUserSerializer):
            serializer.save()
        user = User.objects.get(email=serializer.data['email'])
        conf = str(user.confirmation_code)

        # отправка письма
        send_mail(
            'Registration on the YAMDB',  # тема
            conf,   # текст
            'YAMDB',  # от кого
            [user.email],  # кому
            fail_silently=False,  # «молчать ли об ошибках»
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def send_jwt(request):
    """Получение JWT по запросу с username и confirmation_code """
    serializer = JWTSerializer(data=request.data)
    if serializer.is_valid():
        if not User.objects.filter(
            username=serializer.data.get('username')
        ).exists():
            return Response(
                'Пользователь не найден',
                status=status.HTTP_404_NOT_FOUND
            )
        user = User.objects.get(username=serializer.data['username'])
        # проверка кода
        if serializer.data['confirmation_code'] == str(
            user.confirmation_code
        ):
            return Response(
                f'token: {get_tokens_for_user(user)}',
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                'confirmation_code неверный',
                status=status.HTTP_400_BAD_REQUEST
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def self_patch_user(request):
    """Функция для самостоятельного редактирования учетной записи."""
    # получаем пользователя по JWT
    user = get_object_or_404(User, id=request.user.id)
    if request.method == 'PATCH':
        serializer = PatchUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = FullUserSerializer(user)
    return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """Вьюсет для пользователей."""
    queryset = User.objects.all()
    serializer_class = FullUserSerializer
    permission_classes = (IsAdmin,)
    # поле для поиска отдельных экземпляров модели, по умолчанию "pk",
    # но нам нужно, чтобы в урлах был username /users/{username}/
    lookup_field = 'username'
