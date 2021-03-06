from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Statistic(models.Model):
    label = models.CharField(max_length=50)
    abbreviated_label = models.CharField(max_length=5)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.label} ({self.abbreviated_label})"


class StatisticOwnership(models.Model):
    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE)
    value = models.IntegerField()

    condition = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f"<{self.statistic}> {'+' if self.value > 0 else '-'}{self.value}"


class Skill(models.Model):
    label = models.CharField(max_length=50)
    description = models.TextField()

    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE)
    costs_double = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.label} ({self.statistic.abbreviated_label}){" (2)" if self.costs_double else ""}'


class SkillOwnership(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    value = models.IntegerField()

    condition = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f"<{self.skill}> {'+' if self.value >= 0 else '-'}{self.value}"


class SkillTreeBranch(models.Model):
    label = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.label

    class Meta:
        verbose_name_plural = "skill tree branches"


class SkillTreeItem(models.Model):
    profession = models.ForeignKey("Profession", on_delete=models.CASCADE)
    branch = models.ForeignKey(SkillTreeBranch, on_delete=models.CASCADE)
    depth = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )
    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE)

    label = models.CharField(max_length=50)
    description = models.TextField()
    impacts = models.ManyToManyField("Impact", blank=True)

    def __str__(self) -> str:
        return f"{self.label} {'+' if self.value >= 0 else '-'}{self.profession}"


class SkillTreeItemOwnership(models.Model):
    skill_tree_item = models.ForeignKey(SkillTreeItem, on_delete=models.CASCADE)
    value = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"<{self.character}> - <{self.skill_tree_item}> - {self.value}"
