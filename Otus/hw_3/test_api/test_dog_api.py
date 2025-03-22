import pytest
from Otus.hw_3.src.dogs import *

def test_all_bread():
    response = dog.all_breads('breeds/list/all')
    assert response.status_code == 200 and response.reason =='OK'


