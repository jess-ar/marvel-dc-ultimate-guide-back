from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    intelligence = models.IntegerField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    durability = models.IntegerField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    combat = models.IntegerField(blank=True, null=True)
    first_appearance = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    alignment = models.CharField(max_length=50, blank=True, null=True)  # good, bad
    gender = models.CharField(max_length=50, blank=True, null=True)
    race = models.CharField(max_length=50, blank=True, null=True)
    height = models.CharField(max_length=50, blank=True, null=True)
    weight = models.CharField(max_length=50, blank=True, null=True)
    eye_color = models.CharField(max_length=50, blank=True, null=True)
    hair_color = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    base = models.CharField(max_length=255, blank=True, null=True)
    group_affiliation = models.TextField(blank=True, null=True)
    relatives = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
