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
    ArmorTypeChoice,
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
    impacts = models.ManyToManyField("Impact")

    def __str__(self) -> str:
        return self.label


class Gear(BaseEquipmentMixin):
    # Gear does not implement anything more
    # than the base class
    pass


class ToolKit(BaseEquipmentMixin):
    concealment = models.CharField(max_length=1, choices=ConcealmentChoice.choices)
    availablility = models.CharField(max_length=1, choices=AvailabilityChoice.choices)
    impacts = models.ManyToManyField("Impact")


class Weapon(BaseEquipmentMixin):
    category = models.CharField(max_length=50, choices=WeaponCategoryChoice.choices)
    damage = models.ForeignKey(DiceRollInformation, on_delete=models.DO_NOTHING)
    damage_type = models.CharField(max_length=1, choices=DamageTypeChoice.choices)
    accuracy = models.IntegerField()

    availablility = models.CharField(max_length=1, choices=AvailabilityChoice.choices)
    reliability = models.IntegerField()
    hands_required = models.IntegerField(choices=HandsRequiredChoice.choices)
    enhancement_spots = models.IntegerField(default=0)

    range = models.CharField(max_length=25)
    effects = models.ManyToManyField(Effect, blank=True)
    concealment = models.CharField(max_length=1, choices=ConcealmentChoice.choices)

    is_elder = models.BooleanField(default=False)


class Ammunition(BaseEquipmentMixin):
    base_quantity = models.IntegerField()
    damage_type = models.CharField(max_length=1, choices=DamageTypeChoice.choices)
    availablility = models.CharField(max_length=1, choices=AvailabilityChoice.choices)
    reliability = models.IntegerField()
    effects = models.ManyToManyField(Effect, blank=True)
    concealment = models.CharField(max_length=1, choices=ConcealmentChoice.choices)

    is_elder = models.BooleanField(default=False)


class Armor(BaseEquipmentMixin):
    category = models.CharField(max_length=50, choices=ArmorCategoryChoice.choices)
    stopping_power = models.IntegerField()
    effects = models.ManyToManyField(Effect, blank=True)

    availablility = models.CharField(max_length=1, choices=AvailabilityChoice.choices)
    reliability = models.IntegerField(null=True)
    enhancement_spots = models.IntegerField(default=0)
    encombrance_value = models.IntegerField(default=0)

    is_elder = models.BooleanField(default=False)


class ArmorEnhancement(BaseEquipmentMixin):
    effects = models.ManyToManyField(Effect, blank=True)
    stopping_power_modifier = models.IntegerField()
    resistances = ArrayField(
        models.CharField(max_length=50, choices=DamageTypeChoice.choices)
    )
