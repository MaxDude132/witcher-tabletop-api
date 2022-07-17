from django.urls import include, path

from rest_framework import routers

from .views import (
    AmmunitionOwnershipViewSet,
    AmmunitionViewSet,
    ArmorEnhancementViewSet,
    ArmorOwnershipViewSet,
    ArmorViewSet,
    DiceRollInformationViewSet,
    EffectOwnershipViewSet,
    EffectViewSet,
    GearOwnsershipViewSet,
    GearViewSet,
    ImpactViewSet,
    RacePerkViewSet,
    RaceViewSet,
    RangeInformationViewSet,
    RegionStandingViewSet,
    ShieldOwnershipViewSet,
    ShieldViewSet,
    SkillOwnershipViewSet,
    SkillViewSet,
    SocialStandingViewSet,
    StatisticOwnershipViewSet,
    StatisticViewSet,
    ToolKitOwnershipViewSet,
    ToolKitViewSet,
    WeaponOwnershipViewSet,
    WeaponViewSet,
)


router = routers.SimpleRouter()
router.register("dice-roll-informations", DiceRollInformationViewSet)
router.register("range-informations", RangeInformationViewSet)
router.register("statistic-ownserships", StatisticOwnershipViewSet)
router.register("statistics", StatisticViewSet)
router.register("skill-ownserships", SkillOwnershipViewSet)
router.register("skills", SkillViewSet)
router.register("impacts", ImpactViewSet)
router.register("effects", EffectViewSet)
router.register("effect-ownerships", EffectOwnershipViewSet)
router.register("gear", GearViewSet)
router.register("gear-ownserships", GearOwnsershipViewSet)
router.register("tool-kits", ToolKitViewSet)
router.register("tool-kit-ownerships", ToolKitOwnershipViewSet)
router.register("weapons", WeaponViewSet)
router.register("weapon-ownserships", WeaponOwnershipViewSet)
router.register("ammunition", AmmunitionViewSet)
router.register("ammunition-ownserships", AmmunitionOwnershipViewSet)
router.register("armor-enhancements", ArmorEnhancementViewSet)
router.register("armor", ArmorViewSet)
router.register("armor-ownserships", ArmorOwnershipViewSet)
router.register("shields", ShieldViewSet)
router.register("shield-ownerships", ShieldOwnershipViewSet)
router.register("races", RaceViewSet)
router.register("social-standings", SocialStandingViewSet)
router.register("region-standings", RegionStandingViewSet)
router.register("race-perks", RacePerkViewSet)

urlpatterns = router.urls
