# Generated by Django 4.0.3 on 2022-07-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0035_remove_ally_player_character_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='shield',
            field=models.ManyToManyField(blank=True, related_name='characters', to='character.shieldownership'),
        ),
        migrations.AlterField(
            model_name='character',
            name='armor',
            field=models.ManyToManyField(blank=True, related_name='characters', to='character.armorownership'),
        ),
    ]