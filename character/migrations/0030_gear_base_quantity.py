# Generated by Django 4.0.3 on 2022-07-13 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("character", "0029_toolkit_effects"),
    ]

    operations = [
        migrations.AddField(
            model_name="gear",
            name="base_quantity",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]