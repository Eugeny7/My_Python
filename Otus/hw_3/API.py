import json
import requests
from pprint import pprint

BASE_URL = 'https://dog.ceo/api'
response = requests.get('https://jsonplaceholder.typicode.com/todos')

info = response.json()
pprint(info)