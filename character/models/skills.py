from django.db import models


class Statistic(models.Model):
    label = models.CharField(max_length=50)
    abbreviated_label = models.CharField(max_length=5)
    description = models.TextField()


class StatisticOwnership(models.Model):
    character = models.ForeignKey('Character', on_delete=models.CASCADE)
    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE)

    value = models.IntegerField()


class Skill(models.Model):
    label = models.CharField(max_length=50)
    description = models.TextField()

    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE)
    costs_double = models.BooleanField()


class SkillOwnership(models.Model):
    character = models.ForeignKey('Character', on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    value = models.IntegerField()
