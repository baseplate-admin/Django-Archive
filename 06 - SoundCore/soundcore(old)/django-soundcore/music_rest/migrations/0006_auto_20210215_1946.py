# Generated by Django 3.1.6 on 2021-02-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music_rest", "0005_auto_20210215_1946"),
    ]

    operations = [
        migrations.AlterField(
            model_name="soundcoremodel",
            name="album_art",
            field=models.CharField(default="-", max_length=200),
        ),
        migrations.AlterField(
            model_name="soundcoremodel",
            name="music_file",
            field=models.CharField(default="-", max_length=200),
        ),
    ]
