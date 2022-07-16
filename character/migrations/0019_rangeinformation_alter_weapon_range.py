# Generated by Django 4.0.3 on 2022-07-13 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("character", "0018_alter_dicerollinformation_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="RangeInformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body_multiplier", models.IntegerField(default=0)),
                ("definitive_value", models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name="weapon",
            name="range",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="character.rangeinformation",
            ),
        ),
    ]
