from django.db import models
from characters.models import Character


class Team(models.Model):
    TEAM_UNIVERSE_CHOICES = [
        ('Marvel', 'Marvel'),
        ('DC', 'DC'),
    ]

    name = models.CharField(max_length=100)
    universe = models.CharField(max_length=10, choices=TEAM_UNIVERSE_CHOICES)
    members = models.ManyToManyField(Character, related_name='teams')

    def __str__(self):
        return self.name
