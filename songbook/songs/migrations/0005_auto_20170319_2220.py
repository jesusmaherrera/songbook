# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-20 05:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_song_lyrics_edit_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name=b'Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='SongListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Titulo'),
        ),
        migrations.AddField(
            model_name='songlistitem',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Song'),
        ),
    ]
