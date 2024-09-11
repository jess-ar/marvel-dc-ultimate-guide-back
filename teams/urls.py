from django.urls import path
from .views import get_avengers_characters, get_justice_league_characters

urlpatterns = [
    path('teams/avengers/', get_avengers_characters, name='get_avengers_characters'),
    path('justice-league/', get_justice_league_characters, name='get_justice_league_characters'),
]