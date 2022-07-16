# Generated by Django 4.0.3 on 2022-07-13 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("character", "0030_gear_base_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="gear",
            name="gear_category",
            field=models.CharField(
                choices=[
                    ("general_gear", "General Gear"),
                    ("containers", "Containers"),
                    ("food_and_drinks", "Food & Drinks"),
                    ("clothing", "Clothing"),
                    ("services", "Services"),
                    ("lodging", "Lodging"),
                ],
                default="general_gear",
                max_length=50,
            ),
            preserve_default=False,
        ),
    ]
