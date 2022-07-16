from rest_framework import serializers

from character.models.character import Impact, RacePerk, RegionStanding, SocialStanding
from character.models.skills import Skill, SkillOwnership, Statistic, StatisticOwnership

from .models import Race


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
