# Generated by Django 3.1 on 2020-08-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0014_main_start_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="main_start",
            name="site_creator",
            field=models.TextField(default=" "),
        ),
    ]
