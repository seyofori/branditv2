# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0043_template_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]