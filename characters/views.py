from rest_framework import generics
from .models import Character
from .serializers import CharacterSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http import JsonResponse
import requests
from rest_framework.pagination import PageNumberPagination


class CharacterSearchView(generics.ListAPIView):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        query = self.request.query_params.get('search', None)
        if query:
            return Character.objects.filter(name__icontains=query)
        return Character.objects.none()


def get_multiple_characters(request):
    character_ids = request.GET.getlist('ids')
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
    pagination_class = PageNumberPagination


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
    permission_classes = [IsAuthenticated, IsAdminUser]
