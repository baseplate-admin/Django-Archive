# Generated by Django 3.2 on 2021-05-24 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0010_alter_musiclist_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='musiclist',
            name='mime_type',
            field=models.CharField(default='', max_length=15),
        ),
    ]
