# Generated by Django 4.0.3 on 2022-07-13 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("character", "0019_rangeinformation_alter_weapon_range"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="rangeinformation",
            options={"ordering": ("body_multiplier", "definitive_value")},
        ),
        migrations.AlterUniqueTogether(
            name="rangeinformation",
            unique_together={("body_multiplier", "definitive_value")},
        ),
    ]
