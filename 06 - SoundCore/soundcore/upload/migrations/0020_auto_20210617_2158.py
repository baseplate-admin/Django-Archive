# Generated by Django 3.2.4 on 2021-06-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0019_alter_musiclist_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="musiclist",
            options={"ordering": ("song_name",)},
        ),
        migrations.AddField(
            model_name="musiclist",
            name="genre",
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]