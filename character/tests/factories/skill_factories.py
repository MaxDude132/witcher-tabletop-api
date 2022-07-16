import random
import factory

from character.models.skills import Skill, SkillOwnership, StatisticOwnership

from ...models import Statistic


class StastisticFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Statistic

    label = factory.Faker("word")
    abbreviated_label = factory.Faker("prefix")
    description = factory.Faker("text")


class StatisticOwnershipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StatisticOwnership

    statistic = factory.SubFactory(StastisticFactory)
    value = factory.LazyAttribute(lambda a: random.randrange(-2, 3))


class SkillFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Skill

    label = factory.Faker("word")
    description = factory.Faker("text")

    statistic = factory.SubFactory(StastisticFactory)
    costs_double = factory.Faker("pybool")


class SkillOwnershipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SkillOwnership

    skill = factory.SubFactory(SkillFactory)
    value = factory.LazyAttribute(lambda a: random.randrange(-2, 3))
