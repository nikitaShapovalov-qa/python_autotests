import requests

token = '48ac6f09b45a297ecfa3bd936e1bd62f'
host = 'https://api.pokemonbattle.me:9104'

'''response_create_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "generate",
    "photo": "generate"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_create_pokemon.text)'''

'''response_change_name_pokemon = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "12961",
    "name": "Боксич",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_change_name_pokemon.text)'''

'''response_add_pokemon_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "12961"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_add_pokemon_pokeball.text)'''

'''response_find_pokemon = requests.get(f'{host}/pokemons', params = {'in_pokeball' : '1', 'attack' : '1'})

print(response_find_pokemon.text)'''

'''response_fight = requests.post(f'{host}/battle', json = {
    "attacking_pokemon": "12961",
    "defending_pokemon": "12888"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_fight.text)'''