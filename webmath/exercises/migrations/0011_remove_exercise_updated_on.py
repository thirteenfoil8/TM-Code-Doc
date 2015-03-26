# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0010_auto_20150321_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='updated_on',
        ),
    ]
