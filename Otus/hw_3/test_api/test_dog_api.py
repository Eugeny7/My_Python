import pytest
from Otus.hw_3.src.dogs import *

def test_all_bread():
    response = dog.all_breads('breeds/list/all')
    assert response.status_code == 200 and response.reason =='OK'

@pytest.mark.parametrize('num',
                         [5,10,11,12,15] )
def test_random_brads(num):
    response = dog.random_breads('breeds/image/random', num)
    assert  len (response['message']) == num

@pytest.mark.parametrize('bread',
                         ['terrier', 'springer', 'spitz'])
def test_by_bread(bread):
    response = dog.by_breed(bread)
    assert response['status'] == 'success'

@pytest.mark.parametrize('sub_breads',
                         ['spaniel', 'affenpinscher'])
def test_sub_breads(sub_breads):
    response_all = dog.all_breads('breeds/list/all').json()
    response_sub = dog.sub_breeds(sub_breads)
    assert response_all['message'][sub_breads] == response_sub['message']

@pytest.mark.parametrize(('bread', 'sub_bread', 'num'), [('terrier', 'american', 3)])
def test_sub_breads_random(bread, sub_bread, num):
    response = dog.sub_breeds_random(bread, sub_bread, num)
    assert response['status'] == 'success'