# Generated by Django 3.2 on 2021-05-07 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(default='', max_length=1024, unique=True)),
                ('artist', models.CharField(default='', max_length=1024, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MusicList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(default='', max_length=1024, unique=True)),
                ('bitrate', models.IntegerField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.album')),
            ],
        ),
    ]