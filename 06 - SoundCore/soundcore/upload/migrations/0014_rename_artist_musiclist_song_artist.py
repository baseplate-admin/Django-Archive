# Generated by Django 3.2.4 on 2021-06-14 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0013_rename_date_musiclist_release_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="musiclist",
            old_name="artist",
            new_name="song_artist",
        ),
    ]
