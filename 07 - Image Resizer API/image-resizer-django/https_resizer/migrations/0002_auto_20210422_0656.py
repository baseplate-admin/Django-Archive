# Generated by Django 3.2 on 2021-04-22 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("https_resizer", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Telementry",
            new_name="HttpsModel",
        ),
        migrations.AlterModelOptions(
            name="httpsmodel",
            options={"verbose_name": "Telementry"},
        ),
    ]
