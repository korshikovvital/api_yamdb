from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'usr'
    MODERATOR = 'mdr'
    ADMIN = 'adm'
    ROLES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    ]
    bio = models.TextField(blank=True)
    role = models.CharField(
        max_length=3,
        choices=ROLES,
        default=USER,
    )




class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.IntegerField(default=None, blank=True, null=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True
    )
    genre = models.ManyToManyField(Genre, through='GenreTitle')


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    tilte = models.ForeignKey(Title, on_delete=models.CASCADE)


class Review(models.Model):
    SCORE = [
        (i, i) for i in range(11)
    ]
    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор'
    )
    score = models.IntegerField(
        choices=SCORE,
        verbose_name='Оценка'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    def __str__(self):
        return self.text


class Comments(models.Model):
    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='coments',
        verbose_name='Отзыв'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='coments',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    def __str__(self):
        return self.text
