from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

from .utils import DiceRoll


class ConcealmentChoices(models.TextChoices):
    TINY = 'T', _('Tiny')
    SMALL = 'S', _('Small')
    LARGE = 'L', _('Large')
    CANNOT_HIDE = 'N', _('Cannot hide')


class AvailabilityChoices(models.TextChoices):
    EVERYWHERE = 'E', _('Everywhere')
    COMMON = 'C', _('Common')
    POOR = 'P', _('Poor')
    RARE = 'R', _('Rare')


class DamageTypeChoices(models.TextChoices):
    SLASHING = 'S', _('Slashing')
    PIERCING = 'P', _('Piercing')
    BLUDGEONING = 'B', _('Bludgeoning')
    ELEMENTAL = 'E', _('Elemental')


class HandsRequiredChoices(models.IntegerChoices):
    ONE_HANDED = 1, _('One-handed')
    TWO_HANDED = 2, _('Two-handed')


class WeaponCategoryChoices(models.TextChoices):
    SWORDS = 'swords', _('Swords')
    SMALL_BLADES = 'small_blades', _('Small Blades')
    AXES = 'axes', _('Axes')
    BLUDGEONS = 'bludgeons', _('Bludgeons')
    POLE_ARMS = 'pole_arms', _('Pole Arms')
    STAVES = 'staves', _('Staves')
    THROWN_WEAPONSE = 'thrown_weapons', _('Thrown Weapons')
    BOWS = 'bows', _('Bows')
    CROSSBOWS = 'crossbows', _('Crossbows')


class ArmorCategoryChoices(models.TextChoices):
    HEAD_ARMOR = 'head_armor', _('Head Armor')
    TORSO_ARMOR = 'torso_armor', _('Torso Armor')
    LEG_ARMOR = 'leg_armor', _('Leg Armor')
    SHIELDS = 'shields', _('Shields')


class ArmorTypeChoices(models.TextChoices):
    LIGHT = 'light', _('Light')
    MEDIUM = 'medium', _('Medium')
    HEAVY = 'heavy', _('Heavy')


class BaseEquipmentMixin(models.Model):
    label = models.CharField(max_length=100)
    description = models.TextField(null=True)
    weight = models.FloatField()
    price = models.IntegerField(help_text=_('Price in Redanian crowns'))

    class Meta:
        abstract = True


class Effect(models.Model):
    label = models.CharField(max_length=50)
    description = models.TextField()
    impacts = models.ManyToManyField('Impact')


class Gear(BaseEquipmentMixin):
    # Gear does not implement anything more
    # than the base class
    pass


class ToolKit(BaseEquipmentMixin):
    concealment = models.CharField(max_length=1, choices=ConcealmentChoices.choices)
    availablility = models.CharField(max_length=1, choices=AvailabilityChoices.choices)
    impacts = models.ManyToManyField('Impact')


class Weapon(BaseEquipmentMixin):
    category = models.CharField(max_length=50, choices=WeaponCategoryChoices.choices)
    damage = models.ForeignKey(DiceRoll, on_delete=models.DO_NOTHING)
    damage_type = models.CharField(max_length=1, choices=DamageTypeChoices.choices)
    accuracy = models.IntegerField()

    availablility = models.CharField(max_length=1, choices=AvailabilityChoices.choices)
    reliability = models.IntegerField()
    hands_required = models.IntegerField(choices=HandsRequiredChoices.choices)
    enhancement_spots = models.IntegerField(default=0)

    range = models.CharField(max_length=25)
    effects = models.ManyToManyField(Effect)
    concealment = models.CharField(max_length=1, choices=ConcealmentChoices.choices)

    is_elder = models.BooleanField(default=False)


class Armor(BaseEquipmentMixin):
    category = models.CharField(max_length=50, choices=ArmorCategoryChoices.choices)
    stopping_power = models.IntegerField()
    effects = models.ManyToManyField(Effect)

    availablility = models.CharField(max_length=1, choices=AvailabilityChoices.choices)
    reliability = models.IntegerField(null=True)
    enhancement_spots = models.IntegerField(default=0)
    encombrance_value = models.IntegerField(default=0)

    is_elder = models.BooleanField(default=False)


class ArmorEnhancement(BaseEquipmentMixin):
    effects = models.ManyToManyField(Effect)
    stopping_power_modifier = models.IntegerField()
    resistances = ArrayField(
        models.CharField(max_length=50, choices=DamageTypeChoices.choices)
    )
