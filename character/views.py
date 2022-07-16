from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from character.models.character import Impact, RacePerk, RegionStanding, SocialStanding
from character.models.skills import Skill, SkillOwnership, Statistic, StatisticOwnership

from .models import Race
from .serializers import (
    ImpactSerializer,
    RacePerkSerializer,
    RaceSerializer,
    RegionStandingSerializer,
    SkillOwnershipSerializer,
    SkillSerializer,
    SocialStandingSerializer,
    StatisticOwnershipSerializer,
    StatisticSerializer,
)


# Create your views here.
class RaceViewSet(ReadOnlyModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class RegionStandingViewSet(ReadOnlyModelViewSet):
    queryset = RegionStanding.objects.all()
    serializer_class = RegionStandingSerializer


class SocialStandingViewSet(ReadOnlyModelViewSet):
    queryset = SocialStanding.objects.all()
    serializer_class = SocialStandingSerializer


class RacePerkViewSet(ReadOnlyModelViewSet):
    queryset = RacePerk.objects.all()
    serializer_class = RacePerkSerializer


class ImpactViewSet(ReadOnlyModelViewSet):
    queryset = Impact.objects.all()
    serializer_class = ImpactSerializer


class StatisticOwnershipViewSet(ModelViewSet):
    queryset = StatisticOwnership.objects.all()
    serializer_class = StatisticOwnershipSerializer


class StatisticViewSet(ReadOnlyModelViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer


class SkillOwnershipViewSet(ModelViewSet):
    queryset = SkillOwnership.objects.all()
    serializer_class = SkillOwnershipSerializer


class SkillViewSet(ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
