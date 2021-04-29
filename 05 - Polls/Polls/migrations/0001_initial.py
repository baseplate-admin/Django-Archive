# Generated by Django 3.1.4 on 2020-12-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Poll",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=200)),
                ("option_1", models.CharField(max_length=200)),
                ("option_2", models.CharField(max_length=200)),
                ("option_3", models.CharField(max_length=200)),
                ("option_4", models.CharField(max_length=200)),
                ("option_1_count", models.IntegerField(default=0)),
                ("option_2_count", models.IntegerField(default=0)),
                ("option_3_count", models.IntegerField(default=0)),
                ("option_4_count", models.IntegerField(default=0)),
                ("time", models.CharField(max_length=100)),
            ],
        ),
    ]