from django.contrib import admin

from .models import Category, Genre, GenreTitle, Title


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)


class GenreTitleInline(admin.TabularInline):
    model = GenreTitle
    verbose_name = 'Жанр'
    verbose_name_plural = 'Жанры'
    extra = 1


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'description', 'category')
    search_fields = ('name',)
    list_editable = ('category',)
    list_filter = ('year',)
    inlines = (GenreTitleInline,)

    empty_value_display = '-пусто-'
