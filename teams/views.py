from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Team
from characters.serializers import CharacterSerializer
from rest_framework import status

@api_view(['GET'])
def get_avengers_characters(request):
    try:
        avengers_team = Team.objects.get(name="Avengers")
        characters = avengers_team.members.all()
        serializer = CharacterSerializer(characters, many=True)
        return Response({"characters": serializer.data})
    except Team.DoesNotExist:
        return Response({"error": "Avengers team not found"}, status=404)



@api_view(['GET'])
def get_justice_league_characters(request):
    try:
        justice_league_team = Team.objects.get(name='Justice League')
        # Obtener los personajes a través de la relación 'members'
        characters = justice_league_team.members.all()
        serializer = CharacterSerializer(characters, many=True)
        return Response({'characters': serializer.data})
    except Team.DoesNotExist:
        return Response({'error': 'Justice League team not found'}, status=status.HTTP_404_NOT_FOUND)
