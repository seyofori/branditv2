# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0017_contest_is_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10000000, null=True),
        ),
    ]
