import csv
import os

from django.conf import settings

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__))))
STATICFILES_DIR = os.path.join(os.path.join(BASE_DIR, 'static/'), 'data')


def read_csv(filename):
    data = []
    dirpath = settings.DATAFILES_DIR
    filepath = os.path.join(dirpath, filename)
    with open(filepath, encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data
