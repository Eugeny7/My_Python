from methods import *
from path_file import *
import json
from csv import DictReader

with open(FILE_JSON, 'r') as user_info:
    user = json.load(user_info)

with open(FILE_CSV, 'r') as books_info:
    book = list(DictReader(books_info))

user_data = Users(user)
all_users = user_data.creation_of_users()

book_data = Book(all_users, book)
result = book_data.rest_of_the_books()

with open(RESULT, 'w') as result_file:
    json.dump(result, result_file, indent=3)
