from django.urls import path
from .views import (
    CharacterCreateView,
    CharacterSearchView,
    CharacterListView,
    CharacterDetailView,
    CharacterUpdateView,
    CharacterDeleteView,
    get_multiple_characters
)

urlpatterns = [
    path('characters/', CharacterListView.as_view(), name='character-list'),
    path('characters/search/', CharacterSearchView, name='character-search'),
    path('get-characters/', get_multiple_characters, name='get_multiple_characters'),
    path('characters/create/', CharacterCreateView.as_view(), name='character-create'),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name='character-detail'),
    path('characters/<int:pk>/update/', CharacterUpdateView.as_view(), name='character-update'),
    path('characters/<int:pk>/delete/', CharacterDeleteView.as_view(), name='character-delete'),
]