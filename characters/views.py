from rest_framework import generics
from .models import Character
from .serializers import CharacterSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from marvel_dc_ultimate_guide.api import character_search
from django.http import JsonResponse


def CharacterSearchView(request):
    query = request.GET.get('q')
    if query:
        result = character_search(query)
        return JsonResponse(result, safe=False)
    return JsonResponse({'error': 'No query provided'}, status=400)


def get_multiple_characters(request):
    character_ids = request.GET.getlist('ids')  # Recibe los IDs de la lista en la URL como parámetros
    character_data = []

    for character_id in character_ids:
        response = requests.get(f'{BASE_URL}/{character_id}')
        if response.status_code == 200:
            data = response.json()
            if data['response'] == 'success':
                character_data.append(data)
        else:
            print(f"Error fetching character with ID {character_id}: {response.status_code}")

    return JsonResponse(character_data, safe=False)

#CREATE
class CharacterCreateView(generics.CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


# READ LIST
class CharacterListView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


# READ 1
class CharacterDetailView(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


# UPDATE
class CharacterUpdateView(generics.UpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


#DELETE
class CharacterDeleteView(generics.DestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
