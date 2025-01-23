import pytest
from characters.models import Character


@pytest.mark.django_db
def test_create_character():
    # Given: A character with test data
    character_data = {
        "name": "Spider-Man",
        "full_name": "Peter Parker",
        "intelligence": 90,
        "strength": 85,
        "speed": 80,
        "durability": 75,
        "power": 90,
        "combat": 85,
        "first_appearance": "Amazing Fantasy #15",
        "publisher": "Marvel",
        "alignment": "good",
        "gender": "Male",
        "race": "Human",
        "height": "5'10\"",
        "weight": "167 lbs",
        "eye_color": "Hazel",
        "hair_color": "Brown",
        "occupation": "Photographer",
        "base": "New York City",
        "group_affiliation": "Avengers",
        "relatives": "Aunt May, Uncle Ben",
        "image_url": "http://example.com/spiderman.jpg",
        "universe": "Marvel"
    }

    # When: Create a character in the database
    character = Character.objects.create(**character_data)

    # Then: The character should be correctly created in the database.
    assert character.name == "Spider-Man"
    assert character.full_name == "Peter Parker"
    assert character.intelligence == 90
    assert character.universe == "Marvel"