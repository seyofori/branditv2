# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-24 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0071_achievement_payment_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='requested',
            field=models.BooleanField(default=False),
        ),
    ]
