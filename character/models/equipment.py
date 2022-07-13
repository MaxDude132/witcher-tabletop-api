from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

from .utils import DiceRollInformation

from ..choices import (
    ConcealmentChoice,
    AvailabilityChoice,
    WeaponCategoryChoice,
    DamageTypeChoice,
    HandsRequiredChoice,
    ArmorCategoryChoice,
)


class BaseEquipmentMixin(models.Model):
    label = models.CharField(max_length=100)
    description = models.TextField(null=True)
    weight = models.FloatField()
    price = models.IntegerField(help_text=_("Price in Redanian crowns"))

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.label


class Effect(models.Model):
    label = models.CharField(max_length=50)
    description = models.TextField()
    impacts = models.ManyToManyField("Impact", blank=True)

    def __str__(self) -> str:
        return self.label


class EffectOwnership(models.Model):
    effet = models.ForeignKey(Effect, on_delete=models.CASCADE)
    value = models.IntegerField(null=True, blank=True)


class Gear(BaseEquipmentMixin):
    # Gear does not implement anything more
    # than the base class

    class Meta:
        verbose_name_plural = 'gear'


class ToolKit(BaseEquipmentMixin):
    concealment = models.CharField(max_length=1, choices=ConcealmentChoice.choices)
    availablility = models.CharField(max_length=1, choices=AvailabilityChoice.choices)
    impacts = models.ManyToManyField("Impact")


class Weapon(BaseEquipmentMixin):
    category = models.CharField(max_length=50, choices=WeaponCategoryChoice.choices)
    damage = models.ForeignKey(DiceRollInformation, on_delete=models.DO_NOTHING)
    damage_type = ArrayField(
        models.CharField(max_length=50, choices=DamageTypeChoice.choices)
    )
    accuracy = models.IntegerField()

    availablility = models.CharField(max_length=1, choices=AvailabilityChoice.choices)
    reliability = models.IntegerField()
    hands_required = models.IntegerField(choices=HandsRequiredChoice.choices)
    enhancement_spots = models.IntegerField(default=0)

    range = models.CharField(max_length=25)
    effects = models.ManyToManyField(EffectOwnership, blank=True)
    concealment = models.CharField(max_length=1, choices=ConcealmentChoice.choices)

    is_elder = models.BooleanField(default=False)


class Ammunition(BaseEquipmentMixin):
    base_quantity = models.IntegerField()
    damage_type = ArrayField(
        models.CharField(max_length=50, choices=DamageTypeChoice.choices)
    )
    availablility = models.CharField(max_length=1, choices=AvailabilityChoice.choices)
    reliability = models.IntegerField()
    effects = models.ManyToManyField(EffectOwnership, blank=True)
    concealment = models.CharField(max_length=1, choices=ConcealmentChoice.choices)

    is_elder = models.BooleanField(default=False)


class Armor(BaseEquipmentMixin):
    category = models.CharField(max_length=50, choices=ArmorCategoryChoice.choices)
    stopping_power = models.IntegerField()
    effects = models.ManyToManyField(EffectOwnership, blank=True)

    availablility = models.CharField(max_length=1, choices=AvailabilityChoice.choices)
    reliability = models.IntegerField(null=True)
    enhancement_spots = models.IntegerField(default=0)
    encombrance_value = models.IntegerField(default=0)

    is_elder = models.BooleanField(default=False)


class ArmorEnhancement(BaseEquipmentMixin):
    effects = models.ManyToManyField(EffectOwnership, blank=True)
    stopping_power_modifier = models.IntegerField()
    resistances = ArrayField(
        models.CharField(max_length=50, choices=DamageTypeChoice.choices)
    )
