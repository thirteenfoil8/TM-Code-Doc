# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='comment',
            field=models.CharField(blank=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exercise',
            name='grade',
            field=models.CharField(blank=True, max_length=60),
            preserve_default=True,
        ),
    ]
