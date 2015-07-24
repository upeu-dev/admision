# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('codigo', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Postulante',
                'verbose_name_plural': 'Postulantes',
            },
        ),
    ]
