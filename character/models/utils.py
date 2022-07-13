from django.db import models


class DiceRollInformation(models.Model):
    number_of_dice = models.IntegerField()
    number_of_sides = models.IntegerField()
    modifier = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.number_of_dice}d{self.number_of_sides}{'+{}'.format(self.modifier) if self.modifier else ''}"

    class Meta:
        unique_together = ('number_of_dice', 'number_of_sides', 'modifier')
        ordering = ('number_of_sides', 'number_of_dice', 'modifier')
