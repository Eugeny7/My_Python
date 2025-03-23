import requests

BASE_URL = 'https://dog.ceo/api'
class Dog:
    def __init__(self, url):
        self.url = url

    def main_request(self, end):
        uri = f'{self.url}/{end}'
        response = requests.get(uri)
        return response

    def all_breads(self, end):
        return self.main_request(end)

    def random_breads(self, end, num):
        url = f'{self.url}/{end}/{num}'
        response = requests.get(url)
        return response.json()

    def by_breed(self, bread):
        url = f'{self.url}/breed/{bread}/images'
        response = requests.get(url)
        return response.json()

    def sub_breeds(self, bread):
        url = f'{self.url}/breed/{bread}/list'
        response = requests.get(url)
        return response.json()

    def sub_breeds_random(self, bread, sub_bread, num):
        url = f'{self.url}/breed/{bread}/{sub_bread}/images/random/{num}'
        response = requests.get(url)
        return response.json()

dog = Dog(BASE_URL)