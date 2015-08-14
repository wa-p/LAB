# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_auto_20150814_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='carta_explicativa',
            field=models.CharField(default=b'/home', max_length=30),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='kardex',
            field=models.CharField(default=b'/home', max_length=30),
        ),
    ]
