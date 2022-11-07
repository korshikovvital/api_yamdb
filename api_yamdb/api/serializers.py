from rest_framework import serializers
from reviews.models import User


class FullUserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователей для админа, все поля."""
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )


class CreateUserSerializer(serializers.ModelSerializer):
    """Сериализатор для самостоятельного создания пользователя."""
    class Meta:
        model = User
        fields = ('username', 'email')


# не нравится
class CreateUserByAdminSerializer(serializers.Serializer):
    """Сериализатор получения пользователем кода подтверждения,
    Если его ранее создал администратор. Запись в БД не требуется."""
    username = serializers.CharField(max_length=256)
    email = serializers.EmailField()


class PatchUserSerializer(serializers.ModelSerializer):
    """Сериализатор для самостоятельного редактирования пользователем."""
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )
        read_only_fields = ('role',)


class JWTSerializer(serializers.Serializer):
    """Сериализатор для получения JWT."""
    username = serializers.CharField(max_length=256)
    confirmation_code = serializers.CharField(max_length=256)
