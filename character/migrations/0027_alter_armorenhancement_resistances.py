# Generated by Django 4.0.3 on 2022-07-13 20:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("character", "0026_alter_armor_options_alter_effect_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="armorenhancement",
            name="resistances",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("S", "Slashing"),
                        ("P", "Piercing"),
                        ("B", "Bludgeoning"),
                        ("E", "Elemental"),
                    ],
                    max_length=50,
                ),
                blank=True,
                null=True,
                size=None,
            ),
        ),
    ]
