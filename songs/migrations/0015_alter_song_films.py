# Generated by Django 4.0.4 on 2022-04-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0014_alter_song_films'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='films',
            field=models.ManyToManyField(blank=True, null=True, related_name='songs', through='songs.Context', to='songs.film'),
        ),
    ]
