from django.urls import path
from .views import (
    CharacterCreateView,
    CharacterSearchView,
    CharacterListView,
    CharacterDetailView,
    CharacterUpdateView,
    CharacterDeleteView,
)

urlpatterns = [
    path('', CharacterListView.as_view(), name='character-list'),
    path('search/', CharacterSearchView.as_view(), name='character-search'),
    path('create/', CharacterCreateView.as_view(), name='character-create'),
    path('<int:pk>/', CharacterDetailView.as_view(), name='character-detail'),
    path('<int:pk>/update/', CharacterUpdateView.as_view(), name='character-update'),
    path('<int:pk>/delete/', CharacterDeleteView.as_view(), name='character-delete'),
]
