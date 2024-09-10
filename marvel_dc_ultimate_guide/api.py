import requests
from decouple import config

API_KEY = config('SUPERHERO_API_KEY')
BASE_URL = f'https://superheroapi.com/api/{API_KEY}'


CHARACTER_IDS = [
    "1", "3", "4", "6", "9", "75", "79", "96", "99", "106", "112", "115", "119",
    "145", "149", "156", "162", "196", "201", "213", "222", "226", "234", "238",
    "241", "274", "275", "280", "303", "314", "332", "3", "14", "17", "20", "32",
    "38", "46", "50", "58", "60", "63", "69", "76", "81", "95", "97", "194", "204",
    "214", "230", "246", "253", "263", "278", "298", "306", "309", "370", "405", "432"
]


def get_all_character_names(ids):
    character_names = []
    for character_id in ids:
        response = requests.get(f'{BASE_URL}/{character_id}')
        if response.status_code == 200:
            data = response.json()
            if data['response'] == 'success':
                character_names.append(data.get('name'))
        else:
            print(f"Error fetching character with ID {character_id}: {response.status_code}")
    return character_names


def character_search(name):
    response = requests.get(f'{BASE_URL}/search/{name}')
    if response.status_code == 200:
        return response.json()
    return {'error': response.status_code}
