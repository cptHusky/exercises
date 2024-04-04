import random
import string

import pytest

from exercises_app.constants import LEVEL_CHOICES, TYPE_CHOICES
from .client import Client


@pytest.fixture
def api_client():
    return Client('http://127.0.0.1:8000/api', 'test_user', 'test_pass')


@pytest.fixture(scope='session')
def test_data():
    return {
        'name': ''.join(random.choice(string.ascii_uppercase) for _ in range(5)),
        'description': ''.join(random.choice(string.ascii_uppercase) for _ in range(10)),
        'type': random.choice(list(TYPE_CHOICES.keys())),
        'level': random.choice(list(LEVEL_CHOICES.keys())),
        'duration': f'00:0{random.randint(1, 9)}:00',
        'reps': random.randint(1, 20),
        'sets': random.randint(1, 5)
    }


def test_create_item(api_client, test_data):
    response = api_client.post('/exercises/', data=test_data)
    assert response.status_code == 201

    new_item = response.json()
    test_data |= {'id': new_item['id']}
    created_item = api_client.get(f"/exercises/{new_item['id']}").json()
    assert created_item == test_data


def test_get_all_data_and_compare_last(api_client, test_data):
    response = api_client.get('/exercises/')
    assert response.status_code == 200

    last_added = response.json()[-1]
    assert last_added == test_data


def test_get_by_id(api_client):
    items = api_client.get('/exercises/').json()
    item_to_find = random.choice(items)
    id_to_find = item_to_find['id']
    item = api_client.get(f'/exercises/{id_to_find}').json()
    assert item == item_to_find


def test_edit_data(api_client):
    response = api_client.get('/exercises/')
    item_to_edit = random.choice(response.json())
    new_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    new_reps = random.randint(1, 20)
    new_sets = random.randint(1, 5)
    item_to_edit |= {
        'name': new_name,
        'reps': new_reps,
        'sets': new_sets
    }
    response = api_client.put(f"/exercises/{item_to_edit['id']}/", data=item_to_edit)
    assert response.status_code == 200
    response = api_client.get(f"/exercises/{item_to_edit['id']}/")
    assert response.json() == item_to_edit


def test_delete_data(api_client):
    items = api_client.get('/exercises/').json()
    i = random.randint(0, len(items) - 1)
    item_to_delete = items[i]
    items.pop(i)
    response = api_client.delete(f"/exercises/{item_to_delete['id']}")
    assert response.status_code == 204
    items_after_deletion = api_client.get('/exercises/').json()
    assert items_after_deletion == items


def test_single_param_filter(api_client):
    param = random.choice(list(TYPE_CHOICES.keys()))
    all_items = api_client.get('/exercises/').json()
    filtered_items = []
    for item in all_items:
        if item['type'] == param:
            filtered_items.append(item)
    requested_items = api_client.get(f"/exercises/?type={param}").json()
    assert requested_items == filtered_items


def test_double_param_filter(api_client):
    type_param = random.choice(list(TYPE_CHOICES.keys()))
    level_param = random.choice(list(LEVEL_CHOICES.keys()))
    all_items = api_client.get('/exercises/').json()
    filtered_items = []
    for item in all_items:
        if item['type'] == type_param and item['level'] == level_param:
            filtered_items.append(item)
    requested_items = api_client.get(f"/exercises/?type={type_param}&level={level_param}").json()
    assert requested_items == filtered_items
