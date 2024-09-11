from django.urls import path
from .views import get_avengers_characters

urlpatterns = [
    path('teams/avengers/', get_avengers_characters, name='get_avengers_characters'),
]