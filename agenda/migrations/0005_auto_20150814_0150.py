# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_auto_20150814_0144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitud',
            old_name='estatus_Solicitud',
            new_name='estatus_solicitud',
        ),
    ]
