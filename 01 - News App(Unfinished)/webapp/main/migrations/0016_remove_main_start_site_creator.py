# Generated by Django 3.1 on 2020-08-08 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0015_main_start_site_creator"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="main_start",
            name="site_creator",
        ),
    ]
