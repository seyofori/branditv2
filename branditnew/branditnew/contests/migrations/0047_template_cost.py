# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0046_template_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='cost',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
