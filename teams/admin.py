from django.contrib import admin
from .models import Team
from characters.models import Character
from django import forms


class TeamAdminForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['members'].queryset = Character.objects.filter(universe=self.instance.universe)
        else:
            self.fields['members'].queryset = Character.objects.none()


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    form = TeamAdminForm
    list_display = ('name', 'universe', 'get_members')

    def get_members(self, obj):
        return ", ".join([member.name for member in obj.members.all()])

    get_members.short_description = 'Members'
