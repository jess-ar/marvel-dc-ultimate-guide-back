from rest_framework import serializers
from .models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'full_name', 'first_appearance', 'publisher', 'gender', 'occupation', 'group_affiliation',
                  'relatives', 'universe', 'image_url']
