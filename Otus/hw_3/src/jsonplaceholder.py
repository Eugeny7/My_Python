import requests

BASE_URL = 'https://jsonplaceholder.typicode.com/posts'
DATA = {
    'body': 'Hello',
    'id': '1',
    'title': 'Test',
    'userId': '2'
}


class Requests:
    def __init__(self, url):
        self.url = url

    def get_requests_all(self):
        return requests.get(self.url).json()

    def get_requests_num(self, params):
        return requests.get(self.url, params=f'id={params}')

    def post_requests(self, data):
        body = data
        response = requests.post(self.url, data=body)
        return response

    def put_requests(self, num, data):
        url = f'{self.url}/{num}'
        body = data
        return requests.put(url, data=body)

    def delete_requests(self, num):
        url = f'{self.url}/{num}'
        return requests.delete(url)


item = Requests(BASE_URL)
