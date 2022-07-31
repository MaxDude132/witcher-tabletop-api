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

from character.models.character import Character, Country, DefiningSkill, Impact, Language, LanguageOwnership, Profession, RacePerk, RegionStanding, SocialStanding
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
from character.models.skills import Skill, SkillOwnership, SkillTreeBranch, SkillTreeItem, SkillTreeItemOwnership, Statistic, StatisticOwnership
from character.models.utils import DiceRollInformation, RangeInformation
from core.serializers import PlayerSerializer

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
    # TODO: Add linked_character

    class Meta:
        model = Romance
        fields = (
            "url",
            "id",
            "romance_type",
            "description",
            "linked_character",
        )


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = (
            'url',
            'id',
            'label',
            'region',
        )


class DefiningSkillSerializer(serializers.HyperlinkedModelSerializer):
    statistic = StatisticSerializer()

    class Meta:
        model = DefiningSkill
        fields = (
            'url',
            'id',
            'label',
            'description',
            'statistic',
        )


class ProfessionSerializer(serializers.HyperlinkedModelSerializer):
    starting_skills = SkillSerializer(many=True)
    starting_gear = GearSerializer(many=True)
    starting_weapons = WeaponSerializer(many=True)
    starting_armor = ArmorSerializer(many=True)
    region_standings = RegionStandingSerializer(many=True)

    class Meta:
        model = Profession
        fields = (
            'url',
            'id',
            'label',
            'description',
            'defining_skill',
            'starting_vigor',
            'starting_skills',
            'starting_gear',
            'starting_weapons',
            'starting_armor',
            'starting_novice_spells',
            'starting_novice_invocations',
            'starting_novice_rituals',
            'starting_low_danger_hexes',
            'region_standings',
        )


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = (
            'url',
            'id',
            'label',
            'description',
        )


class LanguageOwnershipSerializer(serializers.HyperlinkedModelSerializer):
    language = LanguageSerializer()

    class Meta:
        model = LanguageOwnership
        fields = (
            'url',
            'id',
            'language',
            'value',
        )


class SkilltreeBranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SkillTreeBranch
        fields = (
            'url',
            'id',
            'label',
        )
        

class SkillTreeItemSerializer(serializers.HyperlinkedModelSerializer):
    profession = ProfessionSerializer()
    statistic = StatisticSerializer()
    impacts = ImpactSerializer(many=True)

    class Meta:
        model = SkillTreeItem
        fields = (
            'url',
            'id',
            'profession',
            'branch',
            'depth',
            'statistic',
            'label',
            'description',
            'impacts',
        )


class SkillTreeItemOwnershipSerializer(serializers.HyperlinkedModelSerializer):
    skill_tree_item = SkillTreeItemSerializer()

    class Meta:
        model = SkillTreeItemOwnership
        fields = (
            'url',
            'id',
            'skill_tree_item',
            'value',
        )


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    player = PlayerSerializer()
    country = CountrySerializer()
    race = RaceSerializer()
    profession = ProfessionSerializer()
    fate_event = FateEventSerializer()
    family_status = FamilyStatusSerializer()
    region_standings = RegionStandingSerializer(many=True)
    statistics = StatisticOwnershipSerializer(many=True)
    skills = SkillOwnershipSerializer(many=True)
    skill_tree_items = SkillTreeItemOwnershipSerializer(many=True)
    languages = LanguageOwnershipSerializer(many=True)
    gear = GearOwnershipSerializer(many=True)
    tool_kits = ToolKitOwnershipSerializer(many=True)
    weapons = WeaponOwnsershipSerializer(many=True)
    ammunition = AmmunitionOwnsershipSerializer(many=True)
    armor = ArmorOwnershipSerializer(many=True)
    shield = ShieldOwnershipSerializer(many=True)
    life_events = LifeEventSerializer(many=True)
    siblings = SiblingSerializer(many=True)
    allies = AllySerializer(many=True)
    enemies = EnemySerializer(many=True)
    romances = RomanceSerializer(many=True)

    class Meta:
        model = Character
        fields = (
            'url',
            'id',
            'player',
            'name',
            'country',
            'city',
            'race',
            'profession',
            'region_standings',
            'statistics',
            'skills',
            'skill_tree_items',
            'languages',
            'improvement_points',
            'gear',
            'tool_kits',
            'weapons',
            'ammunition',
            'armor',
            'shield',
            'fate_event',
            'family_status',
            'life_events',
            'most_influencial_friend',
            'siblings',
            'allies',
            'enemies',
            'romances',
            'clothing',
            'personality',
            'hair_style',
            'affectations',
            'values_person',
            'value',
            'feelings_on_people',
        )


class RaceMinimalSerializer(RaceSerializer):
    class Meta:
        model = Race
        fields = ('id', 'label')


class ProfessionMinimalSerializer(ProfessionSerializer):
    class Meta:
        model = Profession
        fields = ('id', 'label')


class CountryMinimalSerializer(CountrySerializer):
    region = serializers.SerializerMethodField()

    def get_region(self, obj):
        return obj.get_region_display()

    class Meta:
        model = Country
        fields = ('id', 'label', 'region')


class FateEventMinimalSerializer(FateEventSerializer):
    class Meta:
        model = FateEvent
        fields = (
            "id",
            "description",
            "roll",
        )


class FamilyStatusMinimalSerializer(FamilyStatusSerializer):
    class Meta:
        model = FateEvent
        fields = (
            "id",
            "description",
            "roll",
        )


class StatisticMinimalSerializer(StatisticSerializer):
    class Meta:
        model = Statistic
        fields = (
            "id",
            "label",
            "abbreviated_label",
            "description",
        )


class SkillMinimalSerializer(SkillSerializer):
    class Meta:
        model = Skill
        fields = (
            "id",
            "label",
            "description",
            "statistic",
            "costs_double",
        )


class CharacterCreationOptionsSerializer(serializers.Serializer):
    races = serializers.SerializerMethodField()

    def get_races(self, obj):
        return RaceMinimalSerializer(Race.objects.all(), many=True).data

    professions = serializers.SerializerMethodField()

    def get_professions(self, obj):
        return ProfessionMinimalSerializer(Profession.objects.all(), many=True).data

    countries = serializers.SerializerMethodField()

    def get_countries(self, obj):
        return CountryMinimalSerializer(Country.objects.all(), many=True).data

    common_lifepaths = serializers.SerializerMethodField()

    def get_common_lifepaths(self, obj):
        out = {}

        for category in FateEvent.objects.all().distinct('category').values_list('category', flat=True):
            out[category] = {}

            for region_type in FateEvent.objects.all().distinct('region_type').values_list('region_type', flat=True):
                fate_events = FateEvent.objects.filter(category=category, region_type=region_type)
                out[category][region_type] = FateEventMinimalSerializer(fate_events, many=True).data

        out['family_status'] = {}
        for region_type in FamilyStatus.objects.all().distinct('region_type').values_list('region_type', flat=True):
            family_status = FamilyStatus.objects.filter(region_type=region_type)
            out['family_status'][region_type] = FamilyStatusMinimalSerializer(family_status, many=True).data

        return out

    statistics = serializers.SerializerMethodField()

    def get_statistics(self, obj):
        return StatisticMinimalSerializer(Statistic.objects.all(), many=True).data

    skills = serializers.SerializerMethodField()

    def get_skills(self, obj):
        return StatisticMinimalSerializer(Skill.objects.all(), many=True).data
