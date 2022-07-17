from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
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
from character.models.skills import Skill, SkillOwnership, Statistic, StatisticOwnership
from character.models.utils import DiceRollInformation, RangeInformation

from .models import Race
from .serializers import (
    AllySerializer,
    AmmunitionOwnsershipSerializer,
    AmmunitionSerializer,
    ArmorEnhancementSerializer,
    ArmorOwnershipSerializer,
    ArmorSerializer,
    CharacterSerializer,
    CountrySerializer,
    DefiningSkillSerializer,
    DiceRollInformationSerializer,
    EffectSerializer,
    EffectOwnershipSerializer,
    EnemySerializer,
    FamilyStatusSerializer,
    FateEventSerializer,
    GearOwnershipSerializer,
    GearSerializer,
    ImpactSerializer,
    LanguageOwnershipSerializer,
    LanguageSerializer,
    LifeEventSerializer,
    MostInfluencialFriendSerializer,
    ProfessionSerializer,
    RacePerkSerializer,
    RaceSerializer,
    RangeInformationSerializer,
    RegionStandingSerializer,
    RomanceSerializer,
    ShieldOwnershipSerializer,
    ShieldSerializer,
    SiblingSerializer,
    SkillOwnershipSerializer,
    SkillSerializer,
    SocialStandingSerializer,
    StatisticOwnershipSerializer,
    StatisticSerializer,
    ToolKitOwnershipSerializer,
    ToolKitSerializer,
    WeaponOwnsershipSerializer,
    WeaponSerializer,
)


class DiceRollInformationViewSet(ReadOnlyModelViewSet):
    queryset = DiceRollInformation.objects.all()
    serializer_class = DiceRollInformationSerializer


class RangeInformationViewSet(ReadOnlyModelViewSet):
    queryset = RangeInformation.objects.all()
    serializer_class = RangeInformationSerializer


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


class ImpactViewSet(ReadOnlyModelViewSet):
    queryset = Impact.objects.all()
    serializer_class = ImpactSerializer


class EffectViewSet(ReadOnlyModelViewSet):
    queryset = Effect.objects.all()
    serializer_class = EffectSerializer


class EffectOwnershipViewSet(ModelViewSet):
    queryset = EffectOwnership.objects.all()
    serializer_class = EffectOwnershipSerializer


class GearViewSet(ReadOnlyModelViewSet):
    queryset = Gear.objects.all()
    serializer_class = GearSerializer


class GearOwnsershipViewSet(ModelViewSet):
    queryset = GearOwnership.objects.all()
    serializer_class = GearOwnershipSerializer


class ToolKitViewSet(ReadOnlyModelViewSet):
    queryset = ToolKit.objects.all()
    serializer_class = ToolKitSerializer


class ToolKitOwnershipViewSet(ModelViewSet):
    queryset = ToolKitOwnership.objects.all()
    serializer_class = ToolKitOwnershipSerializer


class WeaponViewSet(ReadOnlyModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class WeaponOwnershipViewSet(ModelViewSet):
    queryset = WeaponOwnership.objects.all()
    serializer_class = WeaponOwnsershipSerializer


class AmmunitionViewSet(ReadOnlyModelViewSet):
    queryset = Ammunition.objects.all()
    serializer_class = AmmunitionSerializer


class AmmunitionOwnershipViewSet(ModelViewSet):
    queryset = AmmunitionOwnership.objects.all()
    serializer_class = AmmunitionOwnsershipSerializer


class ArmorEnhancementViewSet(ReadOnlyModelViewSet):
    queryset = ArmorEnhancement.objects.all()
    serializer_class = ArmorEnhancementSerializer


class ArmorViewSet(ReadOnlyModelViewSet):
    queryset = Armor.objects.all()
    serializer_class = ArmorSerializer


class ArmorOwnershipViewSet(ModelViewSet):
    queryset = ArmorOwnership.objects.all()
    serializer_class = ArmorOwnershipSerializer


class ShieldViewSet(ReadOnlyModelViewSet):
    queryset = Shield.objects.all()
    serializer_class = ShieldSerializer


class ShieldOwnershipViewSet(ModelViewSet):
    queryset = ShieldOwnership.objects.all()
    serializer_class = ShieldOwnershipSerializer


class RacePerkViewSet(ReadOnlyModelViewSet):
    queryset = RacePerk.objects.all()
    serializer_class = RacePerkSerializer


class SocialStandingViewSet(ReadOnlyModelViewSet):
    queryset = SocialStanding.objects.all()
    serializer_class = SocialStandingSerializer


class RegionStandingViewSet(ReadOnlyModelViewSet):
    queryset = RegionStanding.objects.all()
    serializer_class = RegionStandingSerializer


class RaceViewSet(ReadOnlyModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class FateEventViewSet(ReadOnlyModelViewSet):
    queryset = FateEvent.objects.all()
    serializer_class = FateEventSerializer


class FamilyStatusViewSet(ReadOnlyModelViewSet):
    queryset = FamilyStatus.objects.all()
    serializer_class = FamilyStatusSerializer


class LifeEventViewSet(ReadOnlyModelViewSet):
    queryset = LifeEvent.objects.all()
    serializer_class = LifeEventSerializer


class MostInfluencialFriendViewSet(ModelViewSet):
    queryset = MostInfluencialFriend.objects.all()
    serializer_class = MostInfluencialFriendSerializer


class SiblingViewSet(ModelViewSet):
    queryset = Sibling.objects.all()
    serializer_class = SiblingSerializer


class AllyViewSet(ModelViewSet):
    queryset = Ally.objects.all()
    serializer_class = AllySerializer


class EnemyViewSet(ModelViewSet):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer


class RomanceViewSet(ModelViewSet):
    queryset = Romance.objects.all()
    serializer_class = RomanceSerializer


"""
Country
Impact
RacePerk
SocialStanding
RegionStanding
Race
DefiningSkill
Profession
Language
Character
LanguageOwnership
"""

class CountryViewSet(ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class DefiningSkillViewSet(ReadOnlyModelViewSet):
    queryset = DefiningSkill.objects.all()
    serializer_class = DefiningSkillSerializer


class ProfessionViewSet(ReadOnlyModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class LanguageViewSet(ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LanguageOwnershipViewSet(ModelViewSet):
    queryset = LanguageOwnership.objects.all()
    serializer_class = LanguageOwnershipSerializer


class CharacterViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
