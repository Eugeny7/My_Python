import os

FILE_JSON = 'users.json'
FILE_CSV = 'books.csv'
RESULT = 'result.json'


def path_file(name_file):
    folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, name_file)
