# Generated by Django 3.1.4 on 2020-12-06 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_downloader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtube',
            name='file',
            field=models.TextField(),
        ),
    ]