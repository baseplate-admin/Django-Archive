# Generated by Django 3.2.4 on 2021-06-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_rename_userinput_uservolumeinput"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uservolumeinput",
            name="volume",
            field=models.IntegerField(default=0),
        ),
    ]
