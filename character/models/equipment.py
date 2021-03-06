from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

from .utils import DiceRollInformation, RangeInformation

from ..choices import (
    ConcealmentChoice,
    AvailabilityChoice,
    GearCategoryChoice,
    WeaponCategoryChoice,
    DamageTypeChoice,
    HandsRequiredChoice,
    ArmorCategoryChoice,
    ArmorTypeChoice,
)


class BaseEquipmentMixin(models.Model):
    label = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    weight = models.FloatField()
    price = models.PositiveIntegerField(help_text=_("Price in Redanian crowns"))

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.label


class Effect(models.Model):
    label = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    impacts = models.ManyToManyField("Impact", blank=True)

    def __str__(self) -> str:
        return self.label

    class Meta:
        ordering = ("label",)


class EffectOwnership(models.Model):
    effect = models.ForeignKey(Effect, on_delete=models.CASCADE)
    value = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.effect}{'({})'.format(self.value) if self.value else ''}"

    class Meta:
        unique_together = ("effect", "value")
        ordering = ("effect", "value")


class Gear(BaseEquipmentMixin):
    weight = models.FloatField(null=True, blank=True)
    base_quantity = models.PositiveIntegerField(null=True, blank=True)
    gear_category = models.CharField(max_length=50, choices=GearCategoryChoice.choices)

    class Meta:
        verbose_name_plural = "gear"


class GearOwnership(models.Model):
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class ToolKit(BaseEquipmentMixin):
    concealment = models.CharField(max_length=1, choices=ConcealmentChoice.choices)
    impacts = models.ManyToManyField("Impact", blank=True)
    effects = models.ManyToManyField(EffectOwnership, blank=True)


class ToolKitOwnership(models.Model):
    tool_kit = models.ForeignKey(ToolKit, on_delete=models.CASCADE)


class Weapon(BaseEquipmentMixin):
    category = models.CharField(max_length=50, choices=WeaponCategoryChoice.choices)
    damage = models.ForeignKey(DiceRollInformation, on_delete=models.DO_NOTHING)
    damage_type = ArrayField(
        models.CharField(max_length=50, choices=DamageTypeChoice.choices)
    )
    accuracy = models.IntegerField()

    availablility = models.CharField(max_length=1, choices=AvailabilityChoice.choices)
    reliability = models.PositiveIntegerField()
    hands_required = models.PositiveIntegerField(choices=HandsRequiredChoice.choices)
    enhancement_spots = models.PositiveIntegerField(default=0)

    range = models.ForeignKey(
        RangeInformation, null=True, blank=True, on_delete=models.CASCADE
    )
    effects = models.ManyToManyField(EffectOwnership, blank=True)
    concealment = models.CharField(max_length=1, choices=ConcealmentChoice.choices)

    is_elder = models.BooleanField(default=False)


class WeaponOwnership(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    runes = None


class Ammunition(BaseEquipmentMixin):
    base_quantity = models.PositiveIntegerField()
    damage_type = ArrayField(
        models.CharField(max_length=50, choices=DamageTypeChoice.choices)
    )
    availablility = models.CharField(max_length=1, choices=AvailabilityChoice.choices)
    reliability = models.PositiveIntegerField()
    effects = models.ManyToManyField(EffectOwnership, blank=True)
    concealment = models.CharField(max_length=1, choices=ConcealmentChoice.choices)

    is_elder = models.BooleanField(default=False)


class AmmunitionOwnership(models.Model):
    ammunition = models.ForeignKey(Ammunition, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Armor(BaseEquipmentMixin):
    category = models.CharField(max_length=50, choices=ArmorCategoryChoice.choices)
    armor_type = models.CharField(
        max_length=50, choices=ArmorTypeChoice.choices, default=ArmorTypeChoice.LIGHT
    )
    stopping_power = models.IntegerField()
    effects = models.ManyToManyField(EffectOwnership, blank=True)

    availablility = models.CharField(max_length=1, choices=AvailabilityChoice.choices)
    enhancement_spots = models.PositiveIntegerField(default=0)
    encombrance_value = models.PositiveIntegerField(default=0)

    is_elder = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "armor"


class Shield(BaseEquipmentMixin):
    armor_type = models.CharField(
        max_length=50, choices=ArmorTypeChoice.choices, default=ArmorTypeChoice.LIGHT
    )
    effects = models.ManyToManyField(EffectOwnership, blank=True)

    availablility = models.CharField(max_length=1, choices=AvailabilityChoice.choices)
    reliability = models.PositiveIntegerField()
    enhancement_spots = models.PositiveIntegerField(default=0)
    encombrance_value = models.PositiveIntegerField(default=0)

    is_elder = models.BooleanField(default=False)


class ArmorEnhancement(BaseEquipmentMixin):
    label = models.CharField(max_length=100, unique=True)
    weight = models.FloatField()
    price = models.PositiveIntegerField(help_text=_("Price in Redanian crowns"))

    availablility = models.CharField(max_length=1, choices=AvailabilityChoice.choices)
    effects = models.ManyToManyField(EffectOwnership, blank=True)
    stopping_power_modifier = models.IntegerField()
    resistances = ArrayField(
        models.CharField(max_length=50, choices=DamageTypeChoice.choices),
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.label


class ArmorOwnership(models.Model):
    armor = models.ForeignKey(Armor, on_delete=models.CASCADE)
    enhancements = models.ManyToManyField(ArmorEnhancement, blank=True)


class ShieldOwnership(models.Model):
    shield = models.ForeignKey(Shield, on_delete=models.CASCADE)
    enhancements = models.ManyToManyField(ArmorEnhancement, blank=True)
