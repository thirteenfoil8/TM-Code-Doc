# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_auto_20150107_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='correction',
            name='exercise',
        ),
        migrations.DeleteModel(
            name='Correction',
        ),
        migrations.RemoveField(
            model_name='hint_exo',
            name='exercice',
        ),
        migrations.DeleteModel(
            name='Hint_exo',
        ),
        migrations.DeleteModel(
            name='Hint_type',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.AddField(
            model_name='exercise',
            name='correction',
            field=models.CharField(max_length=200, default='bla'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exercise',
            name='comment',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exercise',
            name='grade',
            field=models.CharField(max_length=60),
            preserve_default=True,
        ),
    ]
