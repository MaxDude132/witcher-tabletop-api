from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from character.models.character import Race
from character.models.skills import StatisticOwnership

from character.tests.factories.character_factories import (
    CharacterFactory,
    ImpactFactory,
    RaceFactory,
    RacePerkFactory,
    RegionStandingFactory,
)
from character.tests.factories.skill_factories import (
    StatisticOwnershipFactory,
    SkillOwnershipFactory,
)

# Create your tests here.
class RaceViewSetTestCase(APITestCase):
    def test_list(self):
        impact = ImpactFactory()
        impact.statistics.add(StatisticOwnershipFactory())
        impact.skills.add(SkillOwnershipFactory())

        perk = RacePerkFactory()
        perk.impacts.add(impact)

        race = RaceFactory(perks=[perk])
        race.region_standings.add(RegionStandingFactory())

        RaceFactory(perks=[perk])

        url = reverse("race-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)
        self.assertIn(
            reverse("race-detail", kwargs={"pk": race.pk}), response.data[0]["url"]
        )


class CharacterViewSetTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.character = CharacterFactory()

    def test_list(self):
        url = reverse("character-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)

    def test_creation_options(self):
        RaceFactory()
        RaceFactory()

        url = reverse("character-creation-options")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
                'races': [race.label for race in Race.objects.all()]
            }
        )
