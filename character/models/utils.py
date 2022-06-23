from django.db import models


class DiceRoll(models.Model):
    number_of_dice = models.IntegerField()
    number_of_sides = models.IntegerField()
    modifier = models.IntegerField()
