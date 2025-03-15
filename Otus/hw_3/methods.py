import requests
from enum import Enum

class BaseNeed(Enum):
    STATUS_CODE = "status_code"
    REASON = "reason"
    BODY = "body"
    HEADERS = "headers"

class BaseUrl:
    def __init__(self, url):
        self.url = url

    def req_get(self, need: BaseNeed):
        response = requests.get(self.url)
        if need == BaseNeed.STATUS_CODE:
            return response.status_code
        elif need == BaseNeed.REASON:
            return response.reason
        elif need == BaseNeed.BODY:
            return response.json()
        elif need == BaseNeed.HEADERS:
            return response.headers
        else:
            raise ValueError(f'"{need}" Not processed')

dog= BaseUrl('https://dog.ceo/api/breeds/list/all')
print(dog.req_get(BaseNeed.BODY))