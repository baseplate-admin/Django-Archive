# Generated by Django 3.1.4 on 2020-12-08 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Polls", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="IpTable",
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
                ("entry_id", models.IntegerField()),
                ("ip", models.CharField(max_length=12)),
            ],
        ),
        migrations.AlterField(
            model_name="poll",
            name="option_1",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="poll",
            name="option_2",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="poll",
            name="option_3",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="poll",
            name="option_4",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="poll",
            name="time",
            field=models.CharField(max_length=28),
        ),
    ]
