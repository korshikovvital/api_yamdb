from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from ...models import Category, Comment, Genre, GenreTitle, Review, Title, User
from ...utils.csv_reader import read_csv


class Command(BaseCommand):
    """Команда для заполнения БД данными из файлов csv.

    Для заполнения пустой БД выполнить python manage.py populatedb
    """

    def handle(self, *args, **options):
        filename_model = {
            'users.csv': User,
            'category.csv': Category,
            'genre.csv': Genre,
            'titles.csv': Title,
            'genre_title.csv': GenreTitle,
            'review.csv': Review,
            'comments.csv': Comment,
        }
        for filename, model in filename_model.items():
            objs = []
            data = read_csv(filename)
            for obj_dict in data:
                if 'author' in obj_dict:
                    obj_dict['author_id'] = obj_dict.pop('author')
                if 'category' in obj_dict:
                    obj_dict['category_id'] = obj_dict.pop('category')
                objs.append(model(**obj_dict))
            try:
                model.objects.bulk_create(objs)
            except IntegrityError:
                self.stdout.write(self.style.ERROR(
                    'Не удалось импортировать данные\n'
                    'Проверьте, что база данных пуста!'
                ))
                break
            else:
                self.stdout.write(self.style.SUCCESS(
                    f'Файл {filename} успешно импортирован'
                ))
