import csv
import os

from django.conf import settings


def read_csv(filename):
    data = []
    dirpath = settings.DATAFILES_DIR
    filepath = os.path.join(dirpath, filename)
    with open(filepath, encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data
