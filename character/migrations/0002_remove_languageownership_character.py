# Generated by Django 4.0.3 on 2022-07-10 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='languageownership',
            name='character',
        ),
    ]