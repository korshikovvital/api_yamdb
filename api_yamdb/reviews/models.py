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
