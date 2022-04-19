# Generated by Django 4.0.4 on 2022-04-19 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0007_remove_song_films'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='Director',
            new_name='director',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='Year',
            new_name='year',
        ),
        migrations.AddField(
            model_name='film',
            name='songs',
            field=models.ManyToManyField(through='songs.Context', to='songs.song'),
        ),
    ]
