### Описание:

Этот проект позволяет закрепить полученные знания по api на базе Django REST Framework. Никакой практической ценности для стороннего пользователя не несет. Графомания в чистом виде.

### Как запустить проект (Windows):

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/madzone1987/api_final_yatube.git
```

```
cd api_final_yatube
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

Запустить проект:

```
python manage.py runserver
```

### Некоторые примеры запросов к API:

добавить