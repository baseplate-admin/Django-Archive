# Generated by Django 3.2 on 2021-05-19 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("soundcore", "0005_auto_20210519_1230"),
    ]

    operations = [
        migrations.CreateModel(
            name="LibraryName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("library_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name="librarygenerator",
            name="library_name",
        ),
        migrations.AddField(
            model_name="librarygenerator",
            name="name",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="soundcore.libraryname",
            ),
            preserve_default=False,
        ),
    ]
