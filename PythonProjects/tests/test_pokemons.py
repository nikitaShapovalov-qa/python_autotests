import requests
import pytest

token = '48ac6f09b45a297ecfa3bd936e1bd62f'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200

def test_name_of_trainer():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 2621})
    assert response.json()['trainer_name'] == 'Пупсич'