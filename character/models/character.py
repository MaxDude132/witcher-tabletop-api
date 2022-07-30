from django.db import models

from core.models import Player

from .skills import (
    SkillTreeItemOwnership,
    Statistic,
    Skill,
    SkillOwnership,
    StatisticOwnership,
)
from .equipment import (
    AmmunitionOwnership,
    ArmorOwnership,
    Gear,
    GearOwnership,
    ShieldOwnership,
    ToolKitOwnership,
    Weapon,
    Armor,
    WeaponOwnership,
)
from .backstory import (
    Ally,
    Enemy,
    FamilyStatus,
    FateEvent,
    LifeEvent,
    MostInfluencialFriend,
    Romance,
    Sibling,
)
from ..choices import RegionChoice, SocialStandingChoice


class Country(models.Model):
    label = models.CharField(max_length=100)
    region = models.CharField(max_length=50, choices=RegionChoice.choices)

    class Meta:
        verbose_name_plural = "countries"
        unique_together = ("label", "region")
        ordering = ('region', 'label')

    def __str__(self) -> str:
        return self.label


class Impact(models.Model):
    statistics = models.ManyToManyField(
        StatisticOwnership, related_name="impacts", blank=True
    )
    skills = models.ManyToManyField(SkillOwnership, related_name="impacts", blank=True)
    stopping_power = models.IntegerField(blank=True, null=True)

    gear = models.ManyToManyField(GearOwnership, blank=True)
    tool_kits = models.ManyToManyField(ToolKitOwnership, blank=True)

    weapon = models.ManyToManyField(WeaponOwnership, blank=True)
    ammunition = models.ManyToManyField(AmmunitionOwnership, blank=True)
    armor = models.ManyToManyField(ArmorOwnership, blank=True)
    shield = models.ManyToManyField(ShieldOwnership, blank=True)

    def __str__(self) -> str:
        base = (
            f"Stopping power: {self.stopping_power}" if self.stopping_power else "",
            f"Statistics: {', '.join(str(value) for value in self.statistics.all())}"
            if self.statistics.exists()
            else "",
            f'Skills: {", ".join(str(value) for value in self.skills.all())}'
            if self.skills.exists()
            else "",
            f'Gear: {", ".join(str(value) for value in self.gear.all())}'
            if self.gear.exists()
            else "",
            f'Tool kits: {", ".join(str(value) for value in self.tool_kits.all())}'
            if self.tool_kits.exists()
            else "",
            f'Weapons: {", ".join(str(value) for value in self.weapon.all())}'
            if self.weapon.exists()
            else "",
            f'Ammunition: {", ".join(str(value) for value in self.ammunition.all())}'
            if self.ammunition.exists()
            else "",
            f'Armor: {", ".join(str(value) for value in self.armor.all())}'
            if self.armor.exists()
            else "",
            f'Shields: {", ".join(str(value) for value in self.shield.all())}'
            if self.shield.exists()
            else "",
        )
        return " - ".join([item for item in base if item])


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
    social_standing = models.ForeignKey(
        SocialStanding, on_delete=models.CASCADE, null=True
    )

    class Meta:
        unique_together = ("region", "social_standing")

    def __str__(self) -> str:
        return f"{self.region.title()} - {self.social_standing.label.title()}"


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

    starting_vigor = models.PositiveIntegerField()
    starting_skills = models.ManyToManyField(Skill, blank=True)
    starting_gear = models.ManyToManyField(Gear, blank=True)
    starting_weapons = models.ManyToManyField(Weapon, blank=True)
    starting_armor = models.ManyToManyField(Armor, blank=True)

    starting_novice_spells = models.PositiveIntegerField()
    starting_novice_invocations = models.PositiveIntegerField()
    starting_novice_rituals = models.PositiveIntegerField()
    starting_low_danger_hexes = models.PositiveIntegerField()

    region_standings = models.ManyToManyField(RegionStanding, blank=True)

    def __str__(self) -> str:
        return self.label


class Language(models.Model):
    label = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.label


class LanguageOwnership(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self) -> str:
        return f"<{self.language} {self.value}>"


class Character(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=150)

    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    region_standings = models.ManyToManyField(
        RegionStanding, related_name="characters", blank=True
    )

    # Stats and Skills
    statistics = models.ManyToManyField(StatisticOwnership, related_name="characters", blank=True)
    skills = models.ManyToManyField(SkillOwnership, related_name="characters", blank=True)
    skill_tree_items = models.ManyToManyField(
        SkillTreeItemOwnership, related_name="characters", blank=True
    )
    languages = models.ManyToManyField(LanguageOwnership, related_name="characters", blank=True)
    improvement_points = models.PositiveIntegerField(default=0)

    # Equipement
    gear = models.ManyToManyField(GearOwnership, related_name="characters", blank=True)
    tool_kits = models.ManyToManyField(
        ToolKitOwnership, related_name="characters", blank=True
    )
    weapons = models.ManyToManyField(
        WeaponOwnership, related_name="characters", blank=True
    )
    ammunition = models.ManyToManyField(
        AmmunitionOwnership, related_name="characters", blank=True
    )
    armor = models.ManyToManyField(
        ArmorOwnership, related_name="characters", blank=True
    )
    shield = models.ManyToManyField(
        ShieldOwnership, related_name="characters", blank=True
    )

    # Backstory
    fate_event = models.ForeignKey(FateEvent, on_delete=models.CASCADE, null=True, blank=True)
    family_status = models.ForeignKey(FamilyStatus, on_delete=models.CASCADE, null=True, blank=True)
    life_events = models.ManyToManyField(
        LifeEvent, related_name="characters", blank=True
    )
    most_influencial_friend = models.OneToOneField(
        MostInfluencialFriend, on_delete=models.SET_NULL, null=True, blank=True
    )
    siblings = models.ManyToManyField(Sibling, related_name="characters", blank=True)
    allies = models.ManyToManyField(Ally, related_name="characters", blank=True)
    enemies = models.ManyToManyField(Enemy, related_name="characters", blank=True)
    romances = models.ManyToManyField(Romance, related_name="characters", blank=True)

    # Personal Style
    clothing = models.CharField(max_length=50, null=True, blank=True)
    personality = models.CharField(max_length=50, null=True, blank=True)
    hair_style = models.CharField(max_length=50, null=True, blank=True)
    affectations = models.CharField(max_length=50, null=True, blank=True)

    # Personal Values
    values_person = models.CharField(max_length=50, null=True, blank=True)
    value = models.CharField(max_length=50, null=True, blank=True)
    feelings_on_people = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.player}"
