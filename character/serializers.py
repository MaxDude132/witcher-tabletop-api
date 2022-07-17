from rest_framework import serializers
from character.choices import GearCategoryChoice
from character.models.backstory import (
    Ally,
    Enemy,
    FamilyStatus,
    FateEvent,
    LifeEvent,
    MostInfluencialFriend,
    Romance,
    Sibling,
)

from character.models.character import Impact, RacePerk, RegionStanding, SocialStanding
from character.models.equipment import (
    Ammunition,
    AmmunitionOwnership,
    Armor,
    ArmorEnhancement,
    ArmorOwnership,
    Effect,
    EffectOwnership,
    Gear,
    GearOwnership,
    Shield,
    ShieldOwnership,
    ToolKit,
    ToolKitOwnership,
    Weapon,
    WeaponOwnership,
)
from character.models.skills import Skill, SkillOwnership, Statistic, StatisticOwnership
from character.models.utils import DiceRollInformation, RangeInformation

from .models import Race


class DiceRollInformationSerializer(serializers.HyperlinkedModelSerializer):
    representation = serializers.SerializerMethodField()

    def get_representation(self, obj):
        return str(obj)

    class Meta:
        model = DiceRollInformation
        fields = (
            "url",
            "id",
            "number_of_dice",
            "number_of_sides",
            "modifier",
            "representation",
        )


class RangeInformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RangeInformation
        fields = (
            "url",
            "id",
            "body_multiplier",
            "definitive_value",
        )


class StatisticSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Statistic
        fields = (
            "url",
            "id",
            "label",
            "abbreviated_label",
            "description",
        )


class StatisticOwnershipSerializer(serializers.HyperlinkedModelSerializer):
    statistic = StatisticSerializer()

    class Meta:
        model = StatisticOwnership
        fields = (
            "url",
            "id",
            "statistic",
            "value",
            "condition",
        )


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    statistic = StatisticSerializer()

    class Meta:
        model = Skill
        fields = (
            "url",
            "id",
            "label",
            "description",
            "statistic",
            "costs_double",
        )


class SkillOwnershipSerializer(serializers.HyperlinkedModelSerializer):
    skill = SkillSerializer()

    class Meta:
        model = SkillOwnership
        fields = (
            "url",
            "id",
            "skill",
            "value",
            "condition",
        )


class ImpactSerializer(serializers.HyperlinkedModelSerializer):
    statistics = StatisticOwnershipSerializer(many=True)
    skills = SkillOwnershipSerializer(many=True)

    class Meta:
        model = Impact
        fields = (
            "url",
            "id",
            "statistics",
            "skills",
            "stopping_power",
            "gear",
            "tool_kits",
            "weapon",
            "ammunition",
            "armor",
            "shield",
        )


class EffectSerializer(serializers.HyperlinkedModelSerializer):
    impacts = ImpactSerializer(many=True)

    class Meta:
        model = Effect
        fields = (
            "url",
            "id",
            "label",
            "description",
            "impacts",
        )


class EffectOwnershipSerializer(serializers.HyperlinkedModelSerializer):
    effect = EffectSerializer()

    class Meta:
        model = EffectOwnership
        fields = (
            "url",
            "id",
            "effect",
            "value",
        )


class GearSerializer(serializers.HyperlinkedModelSerializer):
    gear_category = serializers.ChoiceField(choices=GearCategoryChoice.choices)

    class Meta:
        model = Gear
        fields = (
            "url",
            "id",
            "label",
            "description",
            "weight",
            "price",
            "base_quantity",
            "gear_category",
        )


class GearOwnershipSerializer(serializers.HyperlinkedModelSerializer):
    gear = GearSerializer()

    class Meta:
        model = GearOwnership
        fields = (
            "url",
            "id",
            "gear",
            "quantity",
        )


class ToolKitSerializer(serializers.HyperlinkedModelSerializer):
    impacts = ImpactSerializer(many=True)
    effects = EffectOwnershipSerializer(many=True)

    class Meta:
        model = ToolKit
        fields = (
            "url",
            "id",
            "label",
            "description",
            "weight",
            "price",
            "concealment",
            "impacts",
            "effects",
        )


class ToolKitOwnershipSerializer(serializers.HyperlinkedModelSerializer):
    tool_kit = ToolKitSerializer()

    class Meta:
        model = ToolKitOwnership
        fields = (
            "url",
            "id",
            "tool_kit",
        )


class WeaponSerializer(serializers.HyperlinkedModelSerializer):
    damage = DiceRollInformationSerializer()
    range = RangeInformationSerializer()
    effects = EffectOwnershipSerializer(many=True)

    class Meta:
        model = Weapon
        fields = (
            "url",
            "id",
            "category",
            "damage",
            "damage_type",
            "accuracy",
            "availablility",
            "reliability",
            "hands_required",
            "enhancement_spots",
            "range",
            "effects",
            "concealment",
            "is_elder",
        )


class WeaponOwnsershipSerializer(serializers.HyperlinkedModelSerializer):
    weapon = WeaponSerializer()

    class Meta:
        model = WeaponOwnership
        fields = (
            "url",
            "id",
            "weapon",
            "rune",
        )


"""
shield
"""


class AmmunitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ammunition
        fields = (
            "url",
            "id",
            "base_quantity",
            "damage_type",
            "availablility",
            "reliability",
            "effects",
            "concealment",
            "is_elder",
        )


class AmmunitionOwnsershipSerializer(serializers.HyperlinkedModelSerializer):
    ammunition = AmmunitionSerializer()

    class Meta:
        model = AmmunitionOwnership
        fields = (
            "url",
            "id",
            "ammunition",
            "quantity",
        )


class ArmorEnhancementSerializer(serializers.HyperlinkedModelSerializer):
    effects = EffectOwnershipSerializer(many=True)

    class Meta:
        model = ArmorEnhancement
        fields = (
            "url",
            "id",
            "label",
            "weight",
            "price",
            "availablility",
            "effects",
            "stopping_power_modifier",
            "resistances",
        )


class ArmorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Armor
        fields = (
            "url",
            "id",
            "category",
            "armor_type",
            "stopping_power",
            "effects",
            "availablility",
            "enhancement_spots",
            "encombrance_value",
            "is_elder",
        )


class ArmorOwnershipSerializer(serializers.HyperlinkedModelSerializer):
    armor = ArmorSerializer()
    enhancements = ArmorEnhancementSerializer(many=True)

    class Meta:
        model = ArmorOwnership
        fields = (
            "url",
            "id",
            "armor",
            "enhancements",
        )


class ShieldSerializer(serializers.HyperlinkedModelSerializer):
    effects = EffectOwnershipSerializer(many=True)

    class Meta:
        model = Shield
        fields = (
            "url",
            "id",
            "armor_type",
            "effects",
            "availablility",
            "reliability",
            "enhancement_spots",
            "encombrance_value",
            "is_elder",
        )


class ShieldOwnershipSerializer(serializers.HyperlinkedModelSerializer):
    shield = ShieldSerializer()
    enhancements = ArmorEnhancementSerializer(many=True)

    class Meta:
        model = ShieldOwnership
        fields = (
            "url",
            "id",
            "shield",
            "enhancements",
        )


class RacePerkSerializer(serializers.HyperlinkedModelSerializer):
    impacts = ImpactSerializer(many=True)

    class Meta:
        model = RacePerk
        fields = (
            "url",
            "id",
            "label",
            "description",
            "impacts",
        )


class SocialStandingSerializer(serializers.HyperlinkedModelSerializer):
    impacts = ImpactSerializer(many=True)

    class Meta:
        model = SocialStanding
        fields = (
            "url",
            "id",
            "label",
            "description",
            "impacts",
        )


class RegionStandingSerializer(serializers.HyperlinkedModelSerializer):
    social_standing = SocialStandingSerializer()

    class Meta:
        model = RegionStanding
        fields = (
            "url",
            "id",
            "region",
            "social_standing",
        )


class RaceSerializer(serializers.HyperlinkedModelSerializer):
    region_standings = RegionStandingSerializer(many=True)
    perks = RacePerkSerializer(many=True)

    class Meta:
        model = Race
        fields = (
            "url",
            "id",
            "label",
            "description",
            "region_standings",
            "perks",
        )


class FateEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FateEvent
        fields = (
            "url",
            "id",
            "category",
            "region_type",
            "description",
            "roll",
        )


class FamilyStatusSerializer(serializers.HyperlinkedModelSerializer):
    impacts = ImpactSerializer(many=True)

    class Meta:
        model = FamilyStatus
        fields = (
            "url",
            "id",
            "region_type",
            "status_title",
            "description",
            "starting_gear",
            "roll",
            "impacts",
        )


class LifeEventSerializer(serializers.HyperlinkedModelSerializer):
    impacts = ImpactSerializer(many=True)

    class Meta:
        model = LifeEvent
        fields = (
            "url",
            "id",
            "category",
            "label",
            "description",
            "roll",
            "impacts",
        )


class MostInfluencialFriendSerializer(serializers.HyperlinkedModelSerializer):
    impacts = ImpactSerializer(many=True)
    # TODO: Add linked_character

    class Meta:
        model = MostInfluencialFriend
        fields = (
            "url",
            "id",
            "region_type",
            "status_title",
            "description",
            "starting_gear",
            "roll",
            "impacts",
            "linked_character",
        )


class SiblingSerializer(serializers.HyperlinkedModelSerializer):
    # TODO: Add linked_character

    class Meta:
        model = Sibling
        fields = (
            "url",
            "id",
            "relationship_status",
            "personality",
            "life_status",
            "linked_character",
        )


class AllySerializer(serializers.HyperlinkedModelSerializer):
    # TODO: Add linked_character

    class Meta:
        model = Ally
        fields = (
            "url",
            "id",
            "position",
            "how_you_met",
            "closeness",
            "region",
            "linked_character",
        )


class EnemySerializer(serializers.HyperlinkedModelSerializer):
    # TODO: Add linked_character

    class Meta:
        model = Enemy
        fields = (
            "url",
            "id",
            "position",
            "cause",
            "who_was_wronged",
            "escalation",
            "power_name",
            "power_value",
            "linked_character",
        )


class RomanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Romance
        fields = (
            "url",
            "id",
            "romance_type",
            "description",
            "linked_character",
        )
