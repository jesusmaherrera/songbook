# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='lyrics_formated',
            field=models.TextField(default='', verbose_name=b'Contenido HTML'),
            preserve_default=False,
        ),
    ]
