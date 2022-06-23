from django.db import models

from .equipment import BaseEquipmentMixin, Effect

from ..choices import AvailabilityChoice


class AlchemicalItem(BaseEquipmentMixin):
    availability = models.CharField(max_length=1, choices=AvailabilityChoice.choices)
    effects = models.ManyToManyField(Effect)
