# Generated by Django 4.0.3 on 2022-07-13 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0015_alter_alchemicalitem_effects_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='range',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
