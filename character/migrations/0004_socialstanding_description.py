# Generated by Django 4.0.3 on 2022-07-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("character", "0003_impact_label"),
    ]

    operations = [
        migrations.AddField(
            model_name="socialstanding",
            name="description",
            field=models.TextField(default="TO FILL!"),
            preserve_default=False,
        ),
    ]
