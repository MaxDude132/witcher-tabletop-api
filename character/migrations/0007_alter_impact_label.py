# Generated by Django 4.0.3 on 2022-07-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0006_impact_stopping_power'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impact',
            name='label',
            field=models.CharField(max_length=50),
        ),
    ]
