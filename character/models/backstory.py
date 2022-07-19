from django.db import models
from django.utils.translation import gettext_lazy as _

from ..choices import (
    SexChoice,
    FateEventTypeChoice,
    FateEventRegionTypeChoice,
    LifeEventCategoryChoice,
    AllyRegionChoice,
    WhoWasWrongedChoice,
)


class OtherCharacterMixin(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=SexChoice.choices)
    age = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.name} - {self.sex} - {self.age} years old"


class FateEvent(models.Model):
    category = models.CharField(max_length=50, choices=FateEventTypeChoice.choices)
    region_type = models.CharField(
        max_length=50, choices=FateEventRegionTypeChoice.choices
    )
    description = models.TextField()
    roll = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.description[:50]


class FamilyStatus(models.Model):
    region_type = models.CharField(
        max_length=50, choices=FateEventRegionTypeChoice.choices
    )
    status_title = models.CharField(max_length=50)
    description = models.TextField()

    starting_gear = models.CharField(max_length=50, null=True, blank=True)
    roll = models.PositiveSmallIntegerField(null=True, blank=True)
    impacts = models.ManyToManyField("Impact", blank=True)

    def __str__(self) -> str:
        return self.description[:50]

    class Meta:
        verbose_name_plural = "family status"


class LifeEvent(models.Model):
    category = models.CharField(max_length=50, choices=LifeEventCategoryChoice.choices)
    label = models.CharField(max_length=50)
    description = models.TextField()
    roll = models.PositiveSmallIntegerField(null=True, blank=True)
    impacts = models.ManyToManyField("Impact", blank=True)

    def __str__(self) -> str:
        return self.label


class MostInfluencialFriend(OtherCharacterMixin):
    region_type = models.CharField(
        max_length=50, choices=FateEventRegionTypeChoice.choices
    )
    status_title = models.CharField(max_length=50)
    description = models.TextField()

    starting_gear = models.CharField(max_length=50, null=True, blank=True)
    roll = models.PositiveSmallIntegerField(null=True, blank=True)
    impacts = models.ManyToManyField("Impact", blank=True)
    linked_character = models.OneToOneField(
        "Character",
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="is_most_influencial_friend",
    )


class Sibling(OtherCharacterMixin):
    relationship_status = models.CharField(max_length=50)
    personality = models.CharField(max_length=50)
    life_status = models.CharField(max_length=50)
    linked_character = models.OneToOneField(
        "Character", on_delete=models.CASCADE, null=True, blank=True, related_name="is_sibling"
    )


class Ally(OtherCharacterMixin):
    position = models.CharField(max_length=50)
    how_you_met = models.CharField(max_length=100)
    closeness = models.CharField(max_length=50)
    region = models.CharField(max_length=50, choices=AllyRegionChoice.choices)
    linked_character = models.OneToOneField(
        "Character", on_delete=models.CASCADE, null=True, blank=True, related_name="is_ally"
    )

    class Meta:
        verbose_name_plural = "allies"


class Enemy(OtherCharacterMixin):
    position = models.CharField(max_length=50)
    cause = models.CharField(max_length=100)
    who_was_wronged = models.CharField(
        max_length=5, choices=WhoWasWrongedChoice.choices
    )
    escalation = models.CharField(max_length=100)
    power_name = models.CharField(max_length=50)
    power_value = models.PositiveIntegerField()
    linked_character = models.OneToOneField(
        "Character", on_delete=models.CASCADE, null=True, blank=True, related_name="is_enemy"
    )

    class Meta:
        verbose_name_plural = "enemies"


class Romance(OtherCharacterMixin):
    romance_type = models.CharField(max_length=50)
    description = models.TextField()
    linked_character = models.OneToOneField(
        "Character", on_delete=models.CASCADE, null=True, blank=True, related_name="is_romance"
    )
