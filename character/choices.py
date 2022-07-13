from django.db import models
from django.utils.translation import gettext_lazy as _


# Character
class RegionChoice(models.TextChoices):
    NORTH = "north", _("The North")
    NILFGAARD = "nilfgaard", _("Nilfgaard")
    SKELLIGE = "skellige", _("Skellige")
    DOL_BLATHANNA = "dol_blathanna", _("Dol Blathanna")
    MAHAKAM = "mahakam", _("Mahakam")
    ZERRIKANIA = "zerrikania", _("Zerrikania")
    BEYOND_BOUNDARIES = "beyond_boundaries", _("Beyond the Boundaries")


class SocialStandingChoice(models.TextChoices):
    EQUAL = "equal", _("Equal")
    TOLERATED = "tolerated", _("Tolerated")
    FEARED = "feared", _("Feared")
    HATED = "hated", _("Hated")


class FateEventTypeChoice(models.TextChoices):
    FAMILY_FATE = "family_fate", _(" Family Fate")
    PARENTAL_FATE = "parental_fate", _("Parental Fate")


# Backstory
class FateEventRegionTypeChoice(models.TextChoices):
    NORTHERN_KINGDOMS = "northern_kingdoms", _("The Northern Kingdoms")
    NIFLGAARD = "nilfgaard", _("Nilfgaard")
    ERLDERLANDS = "elderlands", _("Elderlands")


class AllyRegionChoice(models.TextChoices):
    NORTHERN_KINGDOMS = "northern_kingdoms", _("The Northern Kingdoms")
    NIFLGAARD = "nilfgaard", _("Nilfgaard")
    ERLDERLANDS = "elderlands", _("Elderlands")
    BEYOND_BOUNDARIES = "beyond_boundaries", _("Beyond the Boundaries")


class SexChoice(models.TextChoices):
    MALE = "male", _("Male")
    FEMALE = "female", _("Female")


class LifeEventCategoryChoice(models.TextChoices):
    FORTUNE = "fortune", _("Fortune")
    MISFORTUNE = "misfortune", _("Misfortune")


class WhoWasWrongedChoice(models.TextChoices):
    YOU = "you", _("You")
    THEM = "them", _("Them")


# Equipment
class ConcealmentChoice(models.TextChoices):
    TINY = "T", _("Tiny")
    SMALL = "S", _("Small")
    LARGE = "L", _("Large")
    CANNOT_HIDE = "N", _("Cannot hide")


class  AvailabilityChoice(models.TextChoices):
    EVERYWHERE = "E", _("Everywhere")
    COMMON = "C", _("Common")
    POOR = "P", _("Poor")
    RARE = "R", _("Rare")


class DamageTypeChoice(models.TextChoices):
    SLASHING = "S", _("Slashing")
    PIERCING = "P", _("Piercing")
    BLUDGEONING = "B", _("Bludgeoning")
    ELEMENTAL = "E", _("Elemental")


class HandsRequiredChoice(models.IntegerChoices):
    ONE_HANDED = 1, _("One-handed")
    TWO_HANDED = 2, _("Two-handed")


class WeaponCategoryChoice(models.TextChoices):
    SWORDS = "swords", _("Swords")
    SMALL_BLADES = "small_blades", _("Small Blades")
    AXES = "axes", _("Axes")
    BLUDGEONS = "bludgeons", _("Bludgeons")
    POLE_ARMS = "pole_arms", _("Pole Arms")
    STAVES = "staves", _("Staves")
    THROWN_WEAPONSE = "thrown_weapons", _("Thrown Weapons")
    BOWS = "bows", _("Bows")
    CROSSBOWS = "crossbows", _("Crossbows")


class ArmorCategoryChoice(models.TextChoices):
    HEAD_ARMOR = "head_armor", _("Head Armor")
    TORSO_ARMOR = "torso_armor", _("Torso Armor")
    LEG_ARMOR = "leg_armor", _("Leg Armor")


class ArmorTypeChoice(models.TextChoices):
    LIGHT = "light", _("Light")
    MEDIUM = "medium", _("Medium")
    HEAVY = "heavy", _("Heavy")
