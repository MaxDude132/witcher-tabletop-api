from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Statistic(models.Model):
    label = models.CharField(max_length=50)
    abbreviated_label = models.CharField(max_length=5)
    description = models.TextField()


class StatisticOwnership(models.Model):
    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE)

    value = models.IntegerField()


class Skill(models.Model):
    label = models.CharField(max_length=50)
    description = models.TextField()

    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE)
    costs_double = models.BooleanField()


class SkillOwnership(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    value = models.IntegerField()


class SkillTreeItem(models.Model):
    profession = models.ForeignKey('Race', on_delete=models.CASCADE)
    branch = models.IntegerField(validators=[MinValueValidator(1),  MaxValueValidator(3)])
    depth = models.IntegerField(validators=[MinValueValidator(1),  MaxValueValidator(3)])
    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE)

    label = models.CharField(max_length=50)
    description = models.TextField()
    impacts = models.ManyToManyField('Impact')


class SkillTreeItemOwnership(models.Model):
    skill_tree_item = models.ForeignKey(SkillTreeItem, on_delete=models.CASCADE)

    value = models.IntegerField()
