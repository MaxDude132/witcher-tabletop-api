import factory
from character.choices import RegionChoice

from character.models.character import Character, Country, DefiningSkill, Impact, Profession, RacePerk
from character.models.skills import Skill, SkillOwnership, Statistic, StatisticOwnership
from core.tests.factories.player_factory import PlayerFactory

from ...models import Race, RegionStanding, SocialStanding


class ImpactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Impact


class RacePerkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RacePerk

    label = factory.Faker("word")
    description = factory.Faker("text")


class SocialStandingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SocialStanding

    label = factory.Faker("word")
    description = factory.Faker("text")


class RegionStandingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RegionStanding

    region = factory.Faker("word")
    social_standing = factory.SubFactory(SocialStandingFactory)


class RaceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Race

    label = factory.Faker("name")
    description = factory.Faker("text")

    @factory.post_generation
    def perks(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of perks were passed in, use them
            for perk in extracted:
                self.perks.add(perk)


class StatisticFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Statistic

    label = factory.Faker('word')
    abbreviated_label = factory.Faker('currency_code')
    description = factory.Faker('text')


class StatisticOwnershipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StatisticOwnership

    statistic = factory.SubFactory(StatisticFactory)
    value = 0


class SkillFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Skill

    label = factory.Faker('word')
    description = factory.Faker('text')
    statistic = factory.SubFactory(StatisticFactory)
    costs_double = factory.Faker('pybool')


class SkillOwnershipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SkillOwnership

    skill = factory.SubFactory(SkillFactory)
    value = 0


class DefiningSkillFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DefiningSkill

    label = factory.Faker('word')
    description = factory.Faker('text')
    statistic = factory.SubFactory(StatisticFactory)


class ProfessionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profession

    label = factory.Faker('word')
    description = factory.Faker('text')
    defining_skill = factory.SubFactory(DefiningSkillFactory)
    starting_vigor = 0
    starting_novice_spells = 0
    starting_novice_invocations = 0
    starting_novice_rituals = 0
    starting_low_danger_hexes = 0


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    label = factory.Faker('word')
    region = factory.Faker(
        'random_element', elements=[_choice[0] for _choice in RegionChoice.choices]
    )


class CharacterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Character

    player = factory.SubFactory(PlayerFactory)
    name = factory.Faker('name')
    country = factory.SubFactory(CountryFactory)
    city = factory.Faker('word')
    race = factory.SubFactory(RaceFactory)
    profession = factory.SubFactory(ProfessionFactory)
    improvement_points = 0
