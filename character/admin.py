from django.contrib import admin
from character.models.alchemy import AlchemicalItem
from character.models.character import Character, Country, DefiningSkill, Impact, Profession, Race, RacePerk, RegionStanding, SocialStanding, LanguageOwnership
from character.models.equipment import Ammunition, Armor, Effect, Gear, ToolKit, Weapon
from character.models.skills import Skill, SkillOwnership, Statistic, StatisticOwnership, SkillTreeItem, SkillTreeItemOwnership
from character.models.utils import DiceRollInformation


# character
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Impact)
class ImpactAdmin(admin.ModelAdmin):
    pass


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    pass


@admin.register(RacePerk)
class RacePerkAdmin(admin.ModelAdmin):
    pass


@admin.register(SocialStanding)
class SocialStandingAdmin(admin.ModelAdmin):
    pass


@admin.register(RegionStanding)
class RegionStandingAdmin(admin.ModelAdmin):
    pass


@admin.register(DefiningSkill)
class DefiningSkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    pass


@admin.register(LanguageOwnership)
class LanguageOwnershipAdmin(admin.ModelAdmin):
    pass


# skills
@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    pass


@admin.register(StatisticOwnership)
class StastisticOwnershipAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(SkillOwnership)
class SkillOwnershipAdmin(admin.ModelAdmin):
    pass


@admin.register(SkillTreeItem)
class SkillTreeItemAdmin(admin.ModelAdmin):
    pass


@admin.register(SkillTreeItemOwnership)
class SkillTreeItemOwnershipAdmin(admin.ModelAdmin):
    pass


# equipment
@admin.register(Effect)
class EffectAdmin(admin.ModelAdmin):
    pass


@admin.register(Gear)
class GearAdmin(admin.ModelAdmin):
    pass


@admin.register(ToolKit)
class ToolKitAdmin(admin.ModelAdmin):
    pass


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    pass


@admin.register(Ammunition)
class AmmunitionAdmin(admin.ModelAdmin):
    pass


@admin.register(Armor)
class ArmorAdmin(admin.ModelAdmin):
    pass


# utils
@admin.register(DiceRollInformation)
class DiceRollInformationAdmin(admin.ModelAdmin):
    pass


# Alchemy
@admin.register(AlchemicalItem)
class AlchemicalItemAdmin(admin.ModelAdmin):
    pass
