# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_exercise_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise_done',
            name='exercise_done',
            field=models.ForeignKey(to='exercises.Exercise'),
            preserve_default=True,
        ),
    ]
