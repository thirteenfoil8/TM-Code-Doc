# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20150312_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='avatar',
            field=models.ImageField(null=True, blank=True, upload_to='avatars/'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teacher',
            name='avatar',
            field=models.ImageField(null=True, blank=True, upload_to='avatars/'),
            preserve_default=True,
        ),
    ]
