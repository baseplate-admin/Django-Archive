# Generated by Django 3.1 on 2020-08-09 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0019_auto_20200809_0904"),
    ]

    operations = [
        migrations.AddField(
            model_name="main_start",
            name="copyright",
            field=models.CharField(default=" ", max_length=4),
        ),
    ]
