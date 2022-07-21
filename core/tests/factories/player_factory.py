import factory

from core.models import Player


class PlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Player

    username = factory.Faker('word')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
