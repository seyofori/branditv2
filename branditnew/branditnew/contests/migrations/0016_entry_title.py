# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0015_auto_20170918_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
