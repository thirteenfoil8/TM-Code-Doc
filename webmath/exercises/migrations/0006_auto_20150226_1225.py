# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0005_exercise_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='comment',
        ),
        migrations.AddField(
            model_name='exercise',
            name='owner',
            field=models.CharField(default=datetime.datetime(2015, 2, 26, 12, 24, 50, 205096, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise_done',
            name='student',
            field=models.CharField(default=datetime.datetime(2015, 2, 26, 12, 25, 7, 711278, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]
