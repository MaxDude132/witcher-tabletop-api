from rest_framework import routers

from .views import (
    AllyViewSet,
    AmmunitionOwnershipViewSet,
    AmmunitionViewSet,
    ArmorEnhancementViewSet,
    ArmorOwnershipViewSet,
    ArmorViewSet,
    CharacterViewSet,
    CountryViewSet,
    DefiningSkillViewSet,
    DiceRollInformationViewSet,
    EffectOwnershipViewSet,
    EffectViewSet,
    EnemyViewSet,
    FamilyStatusViewSet,
    FateEventViewSet,
    GearOwnsershipViewSet,
    GearViewSet,
    ImpactViewSet,
    LanguageOwnershipViewSet,
    LanguageViewSet,
    LifeEventViewSet,
    MostInfluencialFriendViewSet,
    ProfessionViewSet,
    RacePerkViewSet,
    RaceViewSet,
    RangeInformationViewSet,
    RegionStandingViewSet,
    RomanceViewSet,
    ShieldOwnershipViewSet,
    ShieldViewSet,
    SiblingViewSet,
    SkillOwnershipViewSet,
    SkillTreeBranchViewSet,
    SkillTreeItemOwershipViewSet,
    SkillTreeItemViewSet,
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

# utils
router.register("dice-roll-informations", DiceRollInformationViewSet)
router.register("range-informations", RangeInformationViewSet)

# skills
router.register("statistics", StatisticViewSet)
router.register("statistic-ownerships", StatisticOwnershipViewSet)
router.register("skills", SkillViewSet)
router.register("skill-ownerships", SkillOwnershipViewSet)
router.register("skill-tree-branches", SkillTreeBranchViewSet)
router.register("skill-tree-items", SkillTreeItemViewSet)
router.register("skill-tree=item-ownerships", SkillTreeItemOwershipViewSet)

# equipment
router.register("effects", EffectViewSet)
router.register("effect-ownerships", EffectOwnershipViewSet)
router.register("gear", GearViewSet)
router.register("gear-ownerships", GearOwnsershipViewSet)
router.register("tool-kits", ToolKitViewSet)
router.register("tool-kit-ownerships", ToolKitOwnershipViewSet)
router.register("weapons", WeaponViewSet)
router.register("weapon-ownerships", WeaponOwnershipViewSet)
router.register("ammunition", AmmunitionViewSet)
router.register("ammunition-ownerships", AmmunitionOwnershipViewSet)
router.register("armor-enhancements", ArmorEnhancementViewSet)
router.register("armor", ArmorViewSet)
router.register("armor-ownerships", ArmorOwnershipViewSet)
router.register("shields", ShieldViewSet)
router.register("shield-ownerships", ShieldOwnershipViewSet)

# backstory
router.register("fate-events", FateEventViewSet)
router.register("family-statuses", FamilyStatusViewSet)
router.register("life-events", LifeEventViewSet)
router.register("most-influencial-friends", MostInfluencialFriendViewSet)
router.register("siblings", SiblingViewSet)
router.register("allies", AllyViewSet)
router.register("enemies", EnemyViewSet)
router.register("romances", RomanceViewSet)

# character
router.register("countries", CountryViewSet)
router.register("impacts", ImpactViewSet)
router.register("race-perks", RacePerkViewSet)
router.register("social-standings", SocialStandingViewSet)
router.register("region-standings", RegionStandingViewSet)
router.register("races", RaceViewSet)
router.register("defining-skills", DefiningSkillViewSet)
router.register("professions", ProfessionViewSet)
router.register("languages", LanguageViewSet)
router.register("language-ownerships", LanguageOwnershipViewSet)
router.register("characters", CharacterViewSet)


urlpatterns = router.urls
