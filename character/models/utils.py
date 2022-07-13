from django.db import models


class DiceRollInformation(models.Model):
    number_of_dice = models.IntegerField()
    number_of_sides = models.IntegerField()
    modifier = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.number_of_dice}d{self.number_of_sides}{'+{}'.format(self.modifier) if self.modifier else ''}"
