import factory

from character.models.character import Impact, RacePerk

from ...models import Race, RegionStanding, SocialStanding


class ImpactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Impact


class RacePerkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RacePerk

    label = factory.Faker('word')
    description = factory.Faker('text')


class SocialStandingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SocialStanding

    label = factory.Faker('word')
    description = factory.Faker('text')


class RegionStandingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RegionStanding

    region = factory.Faker('word')
    social_standing = factory.SubFactory(SocialStandingFactory)


class RaceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Race

    label = factory.Faker('name')
    description = factory.Faker('text')

    @factory.post_generation
    def perks(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of perks were passed in, use them
            for perk in extracted:
                self.perks.add(perk)
