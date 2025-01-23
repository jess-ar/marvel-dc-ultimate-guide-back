from django.contrib import admin
from .models import Character
from teams.models import Team


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_name', 'get_universe', 'has_team', 'image_display')

    def get_universe(self, obj):
        return obj.universe

    get_universe.short_description = 'Universe'

    def has_team(self, obj):
        return obj.teams.exists()

    has_team.short_description = 'Has Team'

    def image_display(self, obj):
        if obj.image_url:
            return f'<img src="{obj.image_url}" width="50" height="50" />'
        return "No Image"

    image_display.allow_tags = True
    image_display.short_description = 'Image'
