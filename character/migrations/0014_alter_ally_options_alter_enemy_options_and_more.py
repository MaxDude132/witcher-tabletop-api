# Generated by Django 4.0.3 on 2022-07-13 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0013_skilltreebranch_alter_skilltreeitem_branch'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ally',
            options={'verbose_name_plural': 'allies'},
        ),
        migrations.AlterModelOptions(
            name='enemy',
            options={'verbose_name_plural': 'enemies'},
        ),
        migrations.AlterModelOptions(
            name='familystatus',
            options={'verbose_name_plural': 'family status'},
        ),
        migrations.AlterModelOptions(
            name='gear',
            options={'verbose_name_plural': 'gear'},
        ),
        migrations.AlterModelOptions(
            name='skilltreebranch',
            options={'verbose_name_plural': 'skill tree branches'},
        ),
        migrations.AlterField(
            model_name='effect',
            name='impacts',
            field=models.ManyToManyField(blank=True, to='character.impact'),
        ),
        migrations.CreateModel(
            name='EffectOwnership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True)),
                ('effet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.effect')),
            ],
        ),
        migrations.AlterField(
            model_name='ammunition',
            name='effects',
            field=models.ManyToManyField(blank=True, to='character.effectownership'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='effects',
            field=models.ManyToManyField(blank=True, to='character.effectownership'),
        ),
        migrations.AlterField(
            model_name='armorenhancement',
            name='effects',
            field=models.ManyToManyField(blank=True, to='character.effectownership'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='effects',
            field=models.ManyToManyField(blank=True, to='character.effectownership'),
        ),
    ]
