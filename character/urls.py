from django.urls import include, path

from rest_framework import routers

from .views import (
    ImpactViewSet,
    RacePerkViewSet,
    RaceViewSet,
    RegionStandingViewSet,
    SkillOwnershipViewSet,
    SkillViewSet,
    SocialStandingViewSet,
    StatisticOwnershipViewSet,
    StatisticViewSet,
)


router = routers.SimpleRouter()
router.register("races", RaceViewSet)
router.register("region-standings", RegionStandingViewSet)
router.register("social-standings", SocialStandingViewSet)
router.register("race-perks", RacePerkViewSet)
router.register("impacts", ImpactViewSet)
router.register("statistic-ownserships", StatisticOwnershipViewSet)
router.register("statistics", StatisticViewSet)
router.register("skill-ownserships", SkillOwnershipViewSet)
router.register("skills", SkillViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
