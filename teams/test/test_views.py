import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from teams.models import Team
from characters.models import Character
from teams.serializers import TeamSerializer
from characters.serializers import CharacterSerializer


# Fixture to create an API client
@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_get_avengers_characters(api_client):
    # Given: The Avengers team and its characters are created
    team = Team.objects.create(name="Avengers", universe="Marvel")
    character1 = Character.objects.create(name="Iron Man", full_name="Tony Stark")
    character2 = Character.objects.create(name="Thor", full_name="Thor Odinson")
    team.members.set([character1, character2])

    # When: A request is made to the Avengers characters endpoint
    url = reverse('get_avengers_characters')
    response = api_client.get(url)

    # Then: The response should contain the team characters
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['characters']) == 2
    assert response.data['characters'][0]['name'] == "Iron Man"
    assert response.data['characters'][1]['name'] == "Thor"


@pytest.mark.django_db
def test_get_avengers_characters_not_found(api_client):
    # Given: No Avengers team exists

    # When: A request is made to the Avengers characters endpoint
    url = reverse('get_avengers_characters')
    response = api_client.get(url)

    # Then: The response should indicate that the team was not found
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data['error'] == "Avengers team not found"


@pytest.mark.django_db
def test_get_justice_league_characters(api_client):
    # Given: The Justice League team and its characters are created
    team = Team.objects.create(name="Justice League", universe="DC")
    character1 = Character.objects.create(name="Superman", full_name="Clark Kent")
    character2 = Character.objects.create(name="Batman", full_name="Bruce Wayne")
    team.members.set([character1, character2])

    # When: A request is made to the Justice League characters endpoint
    url = reverse('get_justice_league_characters')
    response = api_client.get(url)

    # Then: The response should contain the team characters
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['characters']) == 2
    assert response.data['characters'][0]['name'] == "Superman"
    assert response.data['characters'][1]['name'] == "Batman"


@pytest.mark.django_db
def test_get_justice_league_characters_not_found(api_client):
    # Given: No Justice League team exists

    # When: A request is made to the Justice League characters endpoint
    url = reverse('get_justice_league_characters')
    response = api_client.get(url)

    # Then: The response should indicate that the team was not found
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data['error'] == "Justice League team not found"
