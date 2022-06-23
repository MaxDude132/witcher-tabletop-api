from unicodedata import category
from django.db import models
from django.utils.translation import gettext_lazy as _

from .character import Character, Impact


class FateEventTypeChoices(models.TextChoices):
    FAMILY_FATE = 'family_fate', _(' Family Fate')
    PARENTAL_FATE = 'parental_fate', _('Parental Fate')


class FateEventRegionTypeChoices(models.TextChoices):
    NORTHERN_KINGDOMS = 'northern_kingdoms', _('Northern Kingdoms')
    NIFLGAARD = 'nilfgaard', _('Nilfgaard')
    ERLDERLANDS = 'elderlands', _('Elderlands')


class SexChoices(models.TextChoices):
    MALE = 'male', _('Male')
    FEMALE = 'female', _('Female')


class LifeEventCategoryChoices(models.TextChoices):
    FORTUNE = 'fortune', _('Fortune')
    MISFORTUNE = 'misfortune', _('Misfortune')


class AllyRegion(FateEventRegionTypeChoices):
    BEYOND_BOUNDARIES = 'beyond_boundaries', _('Beyond the Boundaries')


class WhoWasWrongedChoices(models.TextChoices):
    YOU = 'you', _('You')
    THEM = 'them', _('Them')


class FateEvent(models.Model):
    category = models.CharField(max_length=50, choices=FateEventTypeChoices.choices)
    region_type = models.CharField(max_length=50, choicfes= FateEventRegionTypeChoices.choices)
    description = models.TextField()


class FamilyStatus(models.Model):
    region_type = models.CharField(max_length=50, choicfes= FateEventRegionTypeChoices.choices)
    status_title = models.CharField(max_length=50)
    description = models.TextField()
    impacts = models.ManyToManyField(Impact, on_delete=models.CASCADE)


class MostInfluencialFriend(models.Model):
    region_type = models.CharField(max_length=50, choicfes= FateEventRegionTypeChoices.choices)
    status_title = models.CharField(max_length=50)
    description = models.TextField()
    impacts = models.ManyToManyField(Impact, on_delete=models.CASCADE)


class Sibling(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=SexChoices.choices)
    age = models.IntegerField()
    relationship_status = models.CharField(max_length=50)
    personality = models.CharField(max_length=50)
    life_status = models.CharField(max_length=50)
    linked_character = models.OneToOneField(Character, on_delete=models.CASCADE, null=True)
    player_character = models.ForeignKey(Character, on_delete=models.CASCADE)


class LifeEvent(models.Model):
    category = models.CharField(max_length=50, choices=LifeEventCategoryChoices.choices)
    label = models.CharField(max_length=50)
    description = models.TextField()
    impacts = models.ManyToManyField(Impact)


class Ally(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=SexChoices.choices)
    age = models.IntegerField()
    position = models.CharField(max_length=50)
    how_you_met = models.CharField(max_length=100)
    closeness = models.CharField(max_length=50)
    region = models.CharField(max_length=50, choices=AllyRegion.choices)


class Enemy(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=SexChoices.choices)
    age = models.IntegerField()
    position = models.CharField(max_length=50)
    cause = models.CharField(max_length=100)
    who_was_wronged = models.CharField(max_length=5, choices=WhoWasWrongedChoices.choices)
    escalation = models.CharField(max_length=100)
    power_name = models.CharField(max_length=50)
    power_value = models.IntegerField()
    linked_character = models.OneToOneField(Character, on_delete=models.CASCADE, null=True)
    player_character = models.ForeignKey(Character, on_delete=models.CASCADE)


class Romance(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=SexChoices.choices)
    age = models.IntegerField()
    romance_type = models.CharField(max_length=50)
    description = models.TextField()
    linked_character = models.OneToOneField(Character, on_delete=models.CASCADE, null=True)
    player_character = models.ForeignKey(Character, on_delete=models.CASCADE)
