# Generated by Django 3.1 on 2020-08-09 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20200809_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_start',
            name='name',
            field=models.CharField(default=' ', max_length=15),
        ),
    ]