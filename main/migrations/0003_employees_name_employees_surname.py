# Generated by Django 4.2.3 on 2023-07-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_animals_cage"),
    ]

    operations = [
        migrations.AddField(
            model_name="employees",
            name="name",
            field=models.CharField(default="-", max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="employees",
            name="surname",
            field=models.CharField(default="-", max_length=20),
            preserve_default=False,
        ),
    ]
