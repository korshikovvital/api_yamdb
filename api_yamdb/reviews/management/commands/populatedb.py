from django.core.management.base import BaseCommand

from ...models import (Category, Comments, Genre, GenreTitle, Review, Title,
                       User)
from ...utils.csv_reader import read_csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_model = {
            'category.csv': Category,
            'genre.csv': Genre,
            'users.csv': User
        }
        file_model_ref = {
            'comments.csv': Comments,
            'genre_title.csv': GenreTitle,
            'review.csv': Review,
            'titles.csv': Title
        }
        for file, model in file_model.items():
            objs = []
            data = read_csv(file)
            for obj_dict in data:
                objs.append(model(**obj_dict))
            model.objects.bulk_create(objs)
            self.stdout.write(self.style.SUCCESS(
                f'Файл {file} успешно импортирован'
            ))

        comments = []
        file = 'comments.csv'
        data = read_csv(file)
        for obj_dict in data:
            review_id = obj_dict.pop('review_id')
            author_id = obj_dict.pop('author')
            comment = Comments(**obj_dict)
            review = Review.objects.get(id=review_id)
            author = User.objects.get(id=author_id)
            comment.review_id = review
            comment.author = author
            comments.append(comment)
        Comments.objects.bulk_create(comments)
        self.stdout.write(self.style.SUCCESS(
            f'Файл {file} успешно импортирован'
        ))
