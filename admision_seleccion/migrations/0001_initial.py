# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('codigo', models.CharField(blank=True, null=True, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Postulantes',
                'verbose_name': 'Postulante',
            },
        ),
    ]
