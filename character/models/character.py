from django.db import models

from core.models import Player

from .skills import SkillTreeItem, SkillTreeItemOwnership, Statistic, Skill, SkillOwnership, StatisticOwnership
from .equipment import Ammunition, Gear, ToolKit, Weapon, Armor
from .backstory import FamilyStatus, FateEvent, LifeEvent
from ..choices import RegionChoice, SocialStandingChoice


class Country(models.Model):
    label = models.CharField(max_length=100)
    region = models.CharField(max_length=50, choices=RegionChoice.choices)


class Impact(models.Model):
    statistics = models.ManyToManyField(StatisticOwnership, related_name='impacts')
    skills = models.ManyToManyField(SkillOwnership, related_name='impacts')
    


class RacePerk(models.Model):
    label = models.CharField(max_length=100)
    description = models.TextField()
    impacts = models.ManyToManyField(Impact)


class Race(models.Model):
    label = models.CharField(max_length=100)
    description = models.TextField()

    perk = models.ForeignKey(RacePerk, on_delete=models.CASCADE)


class SocialStanding(models.Model):
    label = models.CharField(max_length=50, choices=SocialStandingChoice.choices)
    region = models.CharField(max_length=50, choices=RegionChoice.choices)
    impacts = models.ManyToManyField(Impact)


class RegionStanding(models.Model):
    region = models.CharField(max_length=50, choices=RegionChoice.choices)
    races = models.ManyToManyField(Race, related_name='social_standings')
    social_standings = models.ManyToManyField(SocialStanding)


class DefiningSkill(models.Model):
    label = models.CharField(max_length=100)
    description = models.TextField()

    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE)


class Profession(models.Model):
    label = models.CharField(max_length=100)
    description = models.TextField()

    defining_skill = models.OneToOneField(DefiningSkill, on_delete=models.CASCADE)

    # TODO: Move starting logic to listeners
    starting_vigor = models.IntegerField()
    starting_skills = models.ManyToManyField(Skill)
    starting_gear = models.ManyToManyField(Gear)
    starting_weapons = models.ManyToManyField(Weapon)
    starting_armor = models.ManyToManyField(Armor)

    starting_novice_spells = models.IntegerField()
    starting_novice_invocations = models.IntegerField()
    starting_novice_rituals = models.IntegerField()
    starting_low_danger_hexes = models.IntegerField()


class Language(models.Model):
    label = models.CharField(max_length=50)
    description = models.TextField()


class Character(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=150)

    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    # Stats and Skills
    statistics = models.ManyToManyField(StatisticOwnership, related_name='characters')
    skills = models.ManyToManyField(SkillOwnership, related_name='characters')
    skill_tree_items = models.ManyToManyField(SkillTreeItemOwnership, related_name='characters')
    languages = models.ManyToManyField('LanguageOwnership', related_name='characters')

    # Equipement
    gear = models.ManyToManyField(Gear, related_name='characters')
    tool_kits = models.ManyToManyField(ToolKit, related_name='characters')
    weapons = models.ManyToManyField(Weapon, related_name='characters')
    ammunition = models.ManyToManyField(Ammunition, related_name='characters')
    armor = models.ManyToManyField(Armor, related_name='characters')

    # Backstory
    fate_event = models.ForeignKey(FateEvent, on_delete=models.CASCADE)
    family_status = models.ForeignKey(FamilyStatus, on_delete=models.CASCADE)
    life_events = models.ManyToManyField(LifeEvent)

    # Personal Style
    clothing = models.CharField(max_length=50, blank=True)
    personality = models.CharField(max_length=50, blank=True)
    hair_style = models.CharField(max_length=50, blank=True)
    affectations = models.CharField(max_length=50, blank=True)
    
    # Personal Values
    values_person = models.CharField(max_length=50, blank=True)
    value = models.CharField(max_length=50, blank=True)
    feelings_on_people = models.CharField(max_length=100, blank=True)   


class LanguageOwnership(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    value = models.IntegerField()
