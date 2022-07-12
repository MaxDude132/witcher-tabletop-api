# Generated by Django 4.0.5 on 2022-07-12 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0012_alter_skilltreeitem_profession'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillTreeBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='skilltreeitem',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='character.skilltreebranch'),
        ),
    ]
