import os
import django
from teams.models import Team
from characters.models import Character

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marvel_dc_ultimate_guide.settings')
django.setup()

avengers, created = Team.objects.get_or_create(
    name="Avengers",
    universe="Marvel"
)
if created:
    print("Avengers team created.")
else:
    print("Avengers team already exists.")

justice_league, created = Team.objects.get_or_create(
    name="Justice League",
    universe="DC"
)
if created:
    print("Justice League team created.")
else:
    print("Justice League team already exists.")

characters_avengers = [
    ("Iron Man", "Tony Stark"),
    ("Thor", "Thor Odinson"),
    ("Captain America", "Steve Rogers"),
    ("Hulk", "Bruce Banner"),
    ("Black Widow", "Natasha Romanoff"),
    ("Hawkeye", "Clint Barton")
]

for character_name, full_name in characters_avengers:
    try:
        character = Character.objects.get(name=character_name, full_name=full_name)
        avengers.members.add(character)
        print(f"{character_name} ({full_name}) added to Avengers.")
    except Character.DoesNotExist:
        print(f"Character {character_name} ({full_name}) not found in the database.")
    except Character.MultipleObjectsReturned:
        print(f"Multiple entries found for {character_name} ({full_name}), please check the database.")

characters_justice_league = [
    ("Superman", "Clark Kent"),
    ("Batman", "Bruce Wayne"),
    ("Wonder Woman", "Diana Prince"),
    ("Flash", "Barry Allen"),
    ("Aquaman", "Orin"),
    ("Cyborg", "Victor Stone")
]

for character_name, full_name in characters_justice_league:
    try:
        character = Character.objects.get(name=character_name, full_name=full_name)
        justice_league.members.add(character)
        print(f"{character_name} ({full_name}) added to Justice League.")
    except Character.DoesNotExist:
        print(f"Character {character_name} ({full_name}) not found in the database.")
    except Character.MultipleObjectsReturned:
        print(f"Multiple entries found for {character_name} ({full_name}), please check the database.")
