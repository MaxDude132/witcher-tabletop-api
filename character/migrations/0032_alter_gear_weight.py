# Generated by Django 4.0.3 on 2022-07-13 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("character", "0031_gear_gear_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gear",
            name="weight",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
