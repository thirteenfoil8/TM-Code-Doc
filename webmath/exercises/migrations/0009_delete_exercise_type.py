# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0008_auto_20150226_1449'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Exercise_type',
        ),
    ]
