from django.db import models


class DiceRollInformation(models.Model):
    number_of_dice = models.IntegerField()
    number_of_sides = models.IntegerField()
    modifier = models.IntegerField()
