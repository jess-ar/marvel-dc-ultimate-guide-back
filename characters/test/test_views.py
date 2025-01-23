import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from characters.models import Character
from django.contrib.auth import get_user_model
from unittest.mock import patch

BASE_URL = "https://superheroapi.com/api"

# Use the custom user model
User = get_user_model()


# Fixture to create an API client
@pytest.fixture
def api_client():
    return APIClient()


# Fixture to create an admin user (including the required email)
@pytest.fixture
def admin_user(db):
    return User.objects.create_superuser(username='admin', email='admin@example.com', password='admin123')


# Fixture to create a sample character for testing
@pytest.fixture
def character():
    return Character.objects.create(
        name="Spider-Man",
        full_name="Peter Parker",
        first_appearance="Amazing Fantasy #15",
        publisher="Marvel",
        gender="Male",
        occupation="Superhero",
        group_affiliation="Avengers",
        relatives="Aunt May, Uncle Ben",
        universe="Marvel"
    )


# Test for creating a character (POST)
@pytest.mark.django_db
def test_create_character(api_client, admin_user):
    # Given: An admin user is authenticated and character data is provided
    api_client.force_authenticate(user=admin_user)
    url = reverse('character-create')
    data = {
        "name": "Iron Man",
        "full_name": "Tony Stark",
        "first_appearance": "Tales of Suspense #39",
        "publisher": "Marvel",
        "gender": "Male",
        "occupation": "Industrialist",
        "group_affiliation": "Avengers",
        "relatives": "Howard Stark, Maria Stark",
        "universe": "Marvel"
    }

    # When: The API request to create a character is made
    response = api_client.post(url, data, format='json')

    # Then: The character should be created successfully
    assert response.status_code == status.HTTP_201_CREATED
    assert Character.objects.filter(name="Iron Man").exists()


# Test for listing characters (GET)
@pytest.mark.django_db
def test_list_characters(api_client, character):
    # Given: There are characters in the database
    url = reverse('character-list')

    # When: The API request to list characters is made
    response = api_client.get(url)

    # Then: The response should contain at least one character
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0


# Test for retrieving character details (GET)
@pytest.mark.django_db
def test_character_detail(api_client, character):
    # Given: A character exists in the database
    url = reverse('character-detail', kwargs={'pk': character.id})

    # When: The API request to retrieve the character details is made
    response = api_client.get(url)

    # Then: The response should return the correct character details
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == "Spider-Man"


# Test for updating a character (PUT)
@pytest.mark.django_db
def test_update_character(api_client, admin_user, character):
    # Given: An admin user is authenticated and the character exists
    api_client.force_authenticate(user=admin_user)
    url = reverse('character-update', kwargs={'pk': character.id})
    data = {
        "name": "Spider-Man",
        "full_name": "Peter Benjamin Parker"
    }

    # When: The API request to update the character is made
    response = api_client.put(url, data, format='json')

    # Then: The character should be updated successfully
    assert response.status_code == status.HTTP_200_OK
    character.refresh_from_db()
    assert character.full_name == "Peter Benjamin Parker"


# Test for deleting a character (DELETE)
@pytest.mark.django_db
def test_delete_character(api_client, admin_user, character):
    # Given: An admin user is authenticated and the character exists
    api_client.force_authenticate(user=admin_user)
    url = reverse('character-delete', kwargs={'pk': character.id})

    # When: The API request to delete the character is made
    response = api_client.delete(url)

    # Then: The character should be deleted successfully
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Character.objects.filter(id=character.id).exists()


@pytest.mark.django_db
def test_character_search_view(api_client):
    # Given: Dos personajes en la base de datos
    Character.objects.create(name="Iron Man")
    Character.objects.create(name="Spider-Man")

    # When: Se realiza una búsqueda con el término "Iron"
    url = reverse('character-search') + '?search=Iron'
    response = api_client.get(url)

    # Then: Solo se debe devolver "Iron Man"
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == "Iron Man"

    # When: Se realiza una búsqueda sin término
    url = reverse('character-search')
    response = api_client.get(url)

    # Then: No se debe devolver ningún resultado
    assert response.status_code == 200
    assert len(response.data) == 0

