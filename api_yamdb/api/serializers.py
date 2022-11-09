from rest_framework import serializers
from reviews.models import (Category, Genre,
                            Title, User,
                            Review,Comments)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class CreateUserByAdminSerializer(serializers.Serializer):
    """Сериализатор получения пользователем кода подтверждения,
    Если его ранее создал администратор. Запись в БД не требуется."""
    username = serializers.CharField(max_length=256)
    email = serializers.EmailField()


class CreateUserSerializer(serializers.ModelSerializer):
    """Сериализатор для самостоятельного создания пользователя."""
    class Meta:
        model = User
        fields = ('username', 'email')


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


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class JWTSerializer(serializers.Serializer):
    """Сериализатор для получения JWT."""
    username = serializers.CharField(max_length=256)
    confirmation_code = serializers.CharField(max_length=256)


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


class TitleGetSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Title
        fields = '__all__'


class TitlePostSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Title
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Comments
        fields = ('id', 'text', 'author', 'pub_date')
