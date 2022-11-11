### Описание:

Этот проект собирает отзывы на произведения. Аутентифицированные пользователи могут оставлять отзывы на произведения, добавленные администраторами проекта. Пользователи также могут оставлять комментарии к отзывам.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/pestrikov/api_yamdb
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Заполнить базу данных тестовыми данными:

```
python manage.py populatedb
```

Запустить проект:

```
python manage.py runserver
```

### Некоторые примеры запросов к API:

_GET_ .../api/v1/categories/

Пример ответа:

```
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "Фильм",
            "slug": "movie"
        },
        ...
    ]
}
```

_POST_ .../api/v1/titles/1/reviews/

```
{
    "text": "Тест",
    "score": 10
}
```

Пример ответа:

```
{
    "id": 1,
    "text": "Тест",
    "author": "admin",
    "score": 10,
    "pub_date": "2022-10-24T08:29:12.186741Z"
}
```

_PATCH_ .../api/v1/titles/1/reviews/1/comments/1

```
{
    "text": "Комментарий"
}
```

Пример ответа:

```
{
    "id": 1,
    "text": "Комментарий",
    "author": "admin",
    "pub_date": "2022-10-24T09:04:42.770603Z"
}
```

### Авторы
Виталий Коршиков, Максим Костров, Павел Пестриков
