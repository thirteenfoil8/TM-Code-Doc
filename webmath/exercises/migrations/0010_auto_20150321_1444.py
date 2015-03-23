# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0009_delete_exercise_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise_done',
            old_name='equation',
            new_name='resolution',
        ),
    ]
