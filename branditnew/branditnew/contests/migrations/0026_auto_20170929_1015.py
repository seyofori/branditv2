# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 10:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0025_auto_20170927_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cost',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
