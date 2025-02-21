import json
from copy import copy
from csv import DictReader
import itertools

from path_file import FILE_CSV, FILE_JSON

with open(FILE_JSON, 'r') as user_info:
    user = json.load(user_info)

with open(FILE_CSV, 'r') as books_info:
    book = list(DictReader(books_info))

equally = len(book) // len(user)
remainder = len(book) % len(user)

users = []


def creation_of_users():
    for name in user:
        input_name = {
            "name": name["name"],
            "gender": name["gender"],
            "address": name["address"],
            "age": name["age"],
            "books": []
        }
        users.append(input_name)


# creation_of_users()
# user_index = 0
# book_index = 0
# book_size_index = len(book)
# for _ in itertools.cycle(users):
#     users[user_index]["books"].append({
#         "title": book[book_index]['Title'],
#         "author": book[book_index]['Author'],
#         "pages": book[book_index]['Pages'],
#         "genre": book[book_index]['Genre']
#     })
#     user_index += 1
#     book_index += 1
#     book_size_index -= 1
#     if user_index == len(users):
#         user_index = 0
#     elif book_index == len(book):
#         book_index = 0
#     elif book_size_index <= 0:
#         break

def distribution_of_books():
    book_index = 0
    user_index = 0
    for _ in users:
        for _ in range(equally):
            users[user_index]["books"].append({
                "title": book[book_index]['Title'],
                "author": book[book_index]['Author'],
                "pages": book[book_index]['Pages'],
                "genre": book[book_index]['Genre']
            })
            book_index += 1
        user_index += 1


def rest_of_the_books():
    book_index = 0
    user_index = 0
    book_copy = copy(book)
    book_copy.reverse()
    for _ in users[:remainder]:
        users[user_index]["books"].append({
            "title": book_copy[book_index]['Title'],
            "author": book_copy[book_index]['Author'],
            "pages": book_copy[book_index]['Pages'],
            "genre": book_copy[book_index]['Genre']
        })
        book_index += 1
        user_index += 1


creation_of_users()
distribution_of_books()
rest_of_the_books()
print()
