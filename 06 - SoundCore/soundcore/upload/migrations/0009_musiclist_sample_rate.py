# Generated by Django 3.2 on 2021-05-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0008_musiclist_music_extension"),
    ]

    operations = [
        migrations.AddField(
            model_name="musiclist",
            name="sample_rate",
            field=models.IntegerField(default=0),
        ),
    ]