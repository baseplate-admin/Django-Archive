# Generated by Django 3.2.4 on 2021-06-18 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0007_alter_uservolumeinput_volume"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserVolumeInput",
        ),
    ]