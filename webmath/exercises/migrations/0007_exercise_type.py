# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0006_auto_20150226_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
