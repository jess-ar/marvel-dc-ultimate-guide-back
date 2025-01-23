import pytest
from teams.models import Team
from django.core.exceptions import ValidationError
from characters.models import Character


@pytest.mark.django_db
def test_create_team():
    # Given: A team is created with a name and a valid universe.
    team = Team.objects.create(name="Avengers", universe="Marvel")

    # Then: The team should be set up correctly
    assert team.name == "Avengers"
    assert team.universe == "Marvel"
    assert team.members.count() == 0


@pytest.mark.django_db
def test_add_members_to_team():
    # Given: Characters are created to add to the team
    character1 = Character.objects.create(name="Iron Man", full_name="Tony Stark")
    character2 = Character.objects.create(name="Thor", full_name="Thor Odinson")

    # When: A team is created and the members are added.
    team = Team.objects.create(name="Avengers", universe="Marvel")
    team.members.add(character1, character2)

    # Then: The team should have the added members
    assert team.members.count() == 2
    assert character1 in team.members.all()
    assert character2 in team.members.all()


@pytest.mark.django_db
def test_team_string_representation():
    team = Team.objects.create(name="Justice League", universe="DC")

    # Test the string representation of the team
    assert str(team) == "Justice League"


@pytest.mark.django_db
def test_team_universe_validation():
    # Given: A team is created with an invalid universe
    team = Team(name="Invalid Team", universe="Unknown")  # Invalid universe

    # When: The team is validated
    # Then: A ValidationError should be raised
    with pytest.raises(ValidationError):
        team.full_clean()