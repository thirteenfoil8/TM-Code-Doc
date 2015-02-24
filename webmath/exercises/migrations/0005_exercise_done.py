# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0004_remove_exercise_donnee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise_done',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('do_on', models.DateTimeField(auto_now_add=True)),
                ('equation', models.CharField(max_length=200)),
                ('exercise_done', models.OneToOneField(to='exercises.Exercise')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
