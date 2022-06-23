from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import Player

from .skills import Statistic, Skill, SkillOwnership, StatisticOwnership
from .equipment import ArmorOwnership, Gear, GearOwnership, ToolKit, ToolKitOwnership, Weapon, Armor, WeaponOwnership
from .backstory import Ally, Enemy, FamilyStatus, FateEvent, LifeEvent, MostInfluencialFriend, Romance, Sibling


class RegionChoice(models.TextChoices):
    NORTH = ('north', _('The North'))
    NILFGAARD = ('nilfgaard', _('Nilfgaard'))
    SKELLIGE = ('skellige', _('Skellige'))
    DOL_BLATHANNA = ('dol_blathanna', _('Dol Blathanna'))
    MAHAKAM = ('mahakam', _('Mahakam'))


class SocialStandingChoices(models.TextChoices):
    EQUAL = ('equal', _('Equal'))
    TOLERATED = ('tolerated', _('Tolerated'))
    FEARED = ('feared', _('Feared'))
    HATED = ('hated', _('Hated'))


class Country(models.Model):
    label = models.CharField(max_length=100)
    region = models.CharField(max_length=50, choices=RegionChoice.choices)


class Impact(models.Model):
    pass


class RacePerk(models.Model):
    label = models.CharField(max_length=100)
    description = models.TextField()
    impacts = models.ManyToManyField(Impact)


class Race(models.Model):
    label = models.CharField(max_length=100)
    description = models.TextField()

    perk = models.ForeignKey(RacePerk, on_delete=models.CASCADE)


class SocialStanding(models.Model):
    label = models.CharField(max_length=50, choices=SocialStandingChoices.choices)
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

    statistics = models.ManyToManyField(Statistic, through=StatisticOwnership, related_name='characters')
    skills = models.ManyToManyField(Skill, through=SkillOwnership, related_name='characters')
    languages = models.ManyToManyField(Language, through='LanguageOwnership', related_name='characters')

    gear = models.ManyToManyField(Gear, related_name='characters')
    tool_kits = models.ManyToManyField(ToolKit, related_name='characters')
    weapons = models.ManyToManyField(Weapon, related_name='characters')
    armor = models.ManyToManyField(Armor, related_name='characters')

    fate_event = models.ForeignKey(FateEvent, on_delete=models.CASCADE)
    family_status = models.ForeignKey(FamilyStatus, on_delete=models.CASCADE)
    most_influencial_friend = models.ForeignKey(MostInfluencialFriend, on_delete=models.CASCADE)
    life_events = models.ManyToManyField(LifeEvent)


class LanguageOwnership(models):
    character = models.ForeignKey(Character)
    language = models.ForeignKey(Language)

    value = models.IntegerField()
