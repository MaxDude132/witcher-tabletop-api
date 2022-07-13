from django.db import models

from .equipment import BaseEquipmentMixin, EffectOwnership

from ..choices import AvailabilityChoice


class AlchemicalItem(BaseEquipmentMixin):
    availability = models.CharField(max_length=1, choices=AvailabilityChoice.choices)
    effects = models.ManyToManyField(EffectOwnership, blank=True)
