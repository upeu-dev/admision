# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('admision_seleccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=60)),
                ('codigo', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Modalidades',
                'verbose_name': 'Modalidad',
            },
        ),
        migrations.AddField(
            model_name='postulante',
            name='modalidad',
            field=models.ForeignKey(to='admision_seleccion.Modalidad', null=True, blank=True),
        ),
    ]
