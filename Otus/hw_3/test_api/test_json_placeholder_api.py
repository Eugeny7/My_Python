from Otus.hw_3.src.jsonplaceholder import *
import pytest

def test_get_item_list():
    response = item.get_requests_all()
    assert response[-1]['id'] == len(response)

@pytest.mark.parametrize('params', [1, 2, 3])
def test_get_item(params):
    response = item.get_requests_num(params).json()
    assert response[0]['id'] == params

def test_post_item():
    response = item.post_requests(DATA)
    assert response.status_code == 201 and response.reason == 'Created'

@pytest.mark.parametrize('num' , [1, 2, 3])
def test_put_item(num):
    response = item.put_requests(num, DATA).json()
    assert response['body'] == DATA['body'] and response['userId'] == DATA['userId']

@pytest.mark.parametrize('num' , [1, 2, 3])
def test_delete_item(num):
    response = item.delete_requests(num)
    assert response.status_code == 200 and response.reason == 'OK'