# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0007_auto_20170829_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='boost',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='entry',
            name='hide',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='entry',
            name='sub',
            field=models.BooleanField(default=False),
        ),
    ]
