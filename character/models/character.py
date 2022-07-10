from pydoc import ModuleScanner
from django.db import models

from core.models import Player

from .skills import SkillTreeItem, SkillTreeItemOwnership, Statistic, Skill, SkillOwnership, StatisticOwnership
from .equipment import Ammunition, Gear, ToolKit, Weapon, Armor
from .backstory import FamilyStatus, FateEvent, LifeEvent
from ..choices import RegionChoice, SocialStandingChoice


class Country(models.Model):
    label = models.CharField(max_length=100)
    region = models.CharField(max_length=50, choices=RegionChoice.choices)

    class Meta:
        verbose_name_plural = "countries"
        unique_together = ('label', 'region')

    def __str__(self) -> str:
        return self.label


class Impact(models.Model):
    label = models.CharField(max_length=50)
    statistics = models.ManyToManyField(StatisticOwnership, related_name='impacts', blank=True)
    skills = models.ManyToManyField(SkillOwnership, related_name='impacts', blank=True)
    stopping_power = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.label


class RacePerk(models.Model):
    label = models.CharField(max_length=100)
    description = models.TextField()
    impacts = models.ManyToManyField(Impact, blank=True)

    def __str__(self) -> str:
        return self.label


class SocialStanding(models.Model):
    label = models.CharField(max_length=50, choices=SocialStandingChoice.choices)
    impacts = models.ManyToManyField(Impact, blank=True)

    description = models.TextField()

    def __str__(self) -> str:
        return self.label.title()


class RegionStanding(models.Model):
    region = models.CharField(max_length=50, choices=RegionChoice.choices)
    social_standing = models.ForeignKey(SocialStanding, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('region', 'social_standing')

    def __str__(self) -> str:
        return f'{self.region.title()} - {self.social_standing.label.title()}'


class Race(models.Model):
    label = models.CharField(max_length=100)
    description = models.TextField()

    region_standings = models.ManyToManyField(RegionStanding, blank=True)
    perks = models.ManyToManyField(RacePerk)

    def __str__(self) -> str:
        return self.label


class DefiningSkill(models.Model):
    label = models.CharField(max_length=100)
    description = models.TextField()

    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.label


class Profession(models.Model):
    label = models.CharField(max_length=100)
    description = models.TextField()

    defining_skill = models.OneToOneField(DefiningSkill, on_delete=models.CASCADE)

    # TODO: Move starting logic to listeners
    starting_vigor = models.IntegerField()
    starting_skills = models.ManyToManyField(Skill, blank=True)
    starting_gear = models.ManyToManyField(Gear, blank=True)
    starting_weapons = models.ManyToManyField(Weapon, blank=True)
    starting_armor = models.ManyToManyField(Armor, blank=True)

    starting_novice_spells = models.IntegerField()
    starting_novice_invocations = models.IntegerField()
    starting_novice_rituals = models.IntegerField()
    starting_low_danger_hexes = models.IntegerField()

    region_standings = models.ManyToManyField(RegionStanding, blank=True)

    def __str__(self) -> str:
        return self.label


class Language(models.Model):
    label = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.label


class Character(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=150)

    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    region_standings = models.ManyToManyField(RegionStanding, blank=True)

    # Stats and Skills
    statistics = models.ManyToManyField(StatisticOwnership, related_name='characters')
    skills = models.ManyToManyField(SkillOwnership, related_name='characters')
    skill_tree_items = models.ManyToManyField(SkillTreeItemOwnership, related_name='characters', blank=True)
    languages = models.ManyToManyField('LanguageOwnership', related_name='characters')

    # Equipement
    gear = models.ManyToManyField(Gear, related_name='characters', blank=True)
    tool_kits = models.ManyToManyField(ToolKit, related_name='characters', blank=True)
    weapons = models.ManyToManyField(Weapon, related_name='characters', blank=True)
    ammunition = models.ManyToManyField(Ammunition, related_name='characters', blank=True)
    armor = models.ManyToManyField(Armor, related_name='characters', blank=True)

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

    def __str__(self) -> str:
        return f'{self.name} - {self.player}' 


class LanguageOwnership(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self) -> str:
        return f'<{self.character}> - <{self.language}>'
