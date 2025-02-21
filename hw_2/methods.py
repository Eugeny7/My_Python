import itertools


class Users:
    def __init__(self, name_list):
        self.name_list = name_list

    def creation_of_users(self):
        users = []
        for name in self.name_list:
            input_name = {
                "name": name["name"],
                "gender": name["gender"],
                "address": name["address"],
                "age": name["age"],
                "books": []
            }
            users.append(input_name)
        return users


class Book:
    def __init__(self, users_list, book_list):
        self.users_list = users_list
        self.book_list = book_list

    def rest_of_the_books(self):
        user_cycle = itertools.cycle(self.users_list)
        for book_info in self.book_list:
            user_list = next(user_cycle)
            user_list["books"].append({
                "title": book_info["Title"],
                "author": book_info["Author"],
                "pages": book_info["Pages"],
                "genre": book_info["Genre"]
            })
        return self.users_list