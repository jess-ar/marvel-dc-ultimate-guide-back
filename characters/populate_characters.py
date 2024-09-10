import os
from dotenv import load_dotenv
from .models import Character
import requests

load_dotenv()

API_KEY = os.getenv('SUPERHERO_API_KEY')
BASE_URL = f'https://superheroapi.com/api/{API_KEY}'


def get_character_data(name):
    response = requests.get(f'{BASE_URL}/search/{name}')
    if response.status_code == 200:
        data = response.json()
        if data['response'] == 'success':
            return data['results'][0]
    return None


def populate_database_with_characters(character_names):
    for name in character_names:
        character_data = get_character_data(name)
        if character_data:
            Character.objects.create(
                name=character_data['name'],
                full_name=character_data['biography'].get('full-name'),
                intelligence=int(character_data['powerstats']['intelligence']) if character_data['powerstats'][
                                                                                      'intelligence'] != 'null' else None,
                strength=int(character_data['powerstats']['strength']) if character_data['powerstats'][
                                                                              'strength'] != 'null' else None,
                speed=int(character_data['powerstats']['speed']) if character_data['powerstats'][
                                                                        'speed'] != 'null' else None,
                durability=int(character_data['powerstats']['durability']) if character_data['powerstats'][
                                                                                  'durability'] != 'null' else None,
                power=int(character_data['powerstats']['power']) if character_data['powerstats'][
                                                                        'power'] != 'null' else None,
                combat=int(character_data['powerstats']['combat']) if character_data['powerstats'][
                                                                          'combat'] != 'null' else None,
                first_appearance=character_data['biography'].get('first-appearance'),
                publisher=character_data['biography'].get('publisher'),
                alignment=character_data['biography'].get('alignment'),
                gender=character_data['appearance'].get('gender'),
                race=character_data['appearance'].get('race'),
                height=', '.join(character_data['appearance'].get('height', [])),
                weight=', '.join(character_data['appearance'].get('weight', [])),
                eye_color=character_data['appearance'].get('eye-color'),
                hair_color=character_data['appearance'].get('hair-color'),
                occupation=character_data['work'].get('occupation'),
                base=character_data['work'].get('base'),
                group_affiliation=character_data['connections'].get('group-affiliation'),
                relatives=character_data['connections'].get('relatives'),
                image_url=character_data['image'].get('url')
            )
