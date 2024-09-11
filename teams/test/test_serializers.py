import pytest
from teams.serializers import TeamSerializer
from teams.models import Team
from characters.models import Character


@pytest.mark.django_db
def test_team_serializer():
    # Given: A team and characters are created
    character1 = Character.objects.create(name="Iron Man", full_name="Tony Stark")
    character2 = Character.objects.create(name="Thor", full_name="Thor Odinson")
    team = Team.objects.create(name="Avengers", universe="Marvel")
    team.members.set([character1, character2])

    # When: The team is serialized
    serializer = TeamSerializer(team)

    # Then: The serialized data should contain the expected fields
    assert serializer.data['name'] == "Avengers"
    assert serializer.data['universe'] == "Marvel"
    assert len(serializer.data['members']) == 2