# Generated by Django 3.1.4 on 2020-12-06 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("youtube_downloader", "0002_auto_20201206_0841"),
    ]

    operations = [
        migrations.AddField(
            model_name="youtube",
            name="short_url",
            field=models.CharField(default="-", max_length=25),
        ),
    ]
