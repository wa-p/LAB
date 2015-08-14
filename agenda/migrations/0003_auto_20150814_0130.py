# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0002_auto_20150813_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('codigo', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('escuela', models.CharField(max_length=30)),
                ('capacidad', models.IntegerField()),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('cod_solicitud', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateField()),
                ('fecha_estimada', models.DateField()),
                ('ci', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='Estatus_Tarea',
            new_name='Estatus_Solicitud',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='estatus_tarea',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='usuario',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='name',
            new_name='ci',
        ),
        migrations.DeleteModel(
            name='Tarea',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='estatus_Solicitud',
            field=models.ForeignKey(to='agenda.Estatus_Solicitud'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='materia',
            field=models.ForeignKey(to='agenda.Materia'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='tipo_solicitud',
            field=models.ForeignKey(to='agenda.Tipo_Solicitud'),
        ),
    ]
