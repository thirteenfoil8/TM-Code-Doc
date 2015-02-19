# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_auto_20150219_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='donnee',
        ),
    ]
