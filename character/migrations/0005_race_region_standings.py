# Generated by Django 4.0.3 on 2022-07-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0004_socialstanding_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='region_standings',
            field=models.ManyToManyField(blank=True, to='character.regionstanding'),
        ),
    ]