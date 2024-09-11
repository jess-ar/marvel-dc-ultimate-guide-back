import pytest
from characters.models import Character
from characters.serializers import CharacterSerializer


@pytest.mark.django_db
class TestCharacterSerializer:
    def test_serialize_character(self):
        # Given: A character instance
        character = Character.objects.create(
            name='Spider-Man',
            full_name='Peter Parker',
            first_appearance='Amazing Fantasy #15',
            publisher='Marvel Comics',
            gender='Male',
            occupation='Superhero, Photographer',
            group_affiliation='Avengers',
            relatives='Aunt May, Uncle Ben',
            universe='Marvel',
            image_url='https://example.com/spiderman.jpg'
        )

        # When: Serializing the character
        serializer = CharacterSerializer(character)
        data = serializer.data

        # Then: Verify that the serialized data matches the character's attributes
        assert data['name'] == 'Spider-Man'
        assert data['full_name'] == 'Peter Parker'
        assert data['first_appearance'] == 'Amazing Fantasy #15'
        assert data['publisher'] == 'Marvel Comics'
        assert data['gender'] == 'Male'
        assert data['occupation'] == 'Superhero, Photographer'
        assert data['group_affiliation'] == 'Avengers'
        assert data['relatives'] == 'Aunt May, Uncle Ben'
        assert data['universe'] == 'Marvel'
        assert data['image_url'] == 'https://example.com/spiderman.jpg'

    def test_deserialize_character(self):
        # Given: Serialized data
        data = {
            'name': 'Iron Man',
            'full_name': 'Tony Stark',
            'first_appearance': 'Tales of Suspense #39',
            'publisher': 'Marvel Comics',
            'gender': 'Male',
            'occupation': 'Industrialist, Inventor',
            'group_affiliation': 'Avengers',
            'relatives': 'Howard Stark, Maria Stark',
            'universe': 'Marvel',
            'image_url': 'https://example.com/ironman.jpg'
        }

        # When: Deserializing the data
        serializer = CharacterSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        character = serializer.save()

        # Then: Verify that the character object was created with the correct attributes
        assert character.name == 'Iron Man'
        assert character.full_name == 'Tony Stark'
        assert character.first_appearance == 'Tales of Suspense #39'
        assert character.publisher == 'Marvel Comics'
        assert character.gender == 'Male'
        assert character.occupation == 'Industrialist, Inventor'
        assert character.group_affiliation == 'Avengers'
        assert character.relatives == 'Howard Stark, Maria Stark'
        assert character.universe == 'Marvel'
        assert character.image_url == 'https://example.com/ironman.jpg'
