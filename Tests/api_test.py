#!/usr/bin/env python3
import requests
import pytest

def test_get_request():
    response = requests.get('https://api.example.com/users')
    assert response.status_code == 200
    assert response.json()['total_users'] > 0

def test_post_request():
    data = {'name': 'John', 'email': 'john@example.com'}
    response = requests.post('https://api.example.com/users', json=data)
    assert response.status_code == 201
    assert response.json()['id'] is not None

def test_invalid_request():
    response = requests.get('https://api.example.com/nonexistent')
    assert response.status_code == 404
    assert 'error' in response.json()

@pytest.mark.parametrize('user_id', [1, 2, 3])
def test_delete_request(user_id):
    response = requests.delete(f'https://api.example.com/users/{user_id}')
    assert response.status_code == 204