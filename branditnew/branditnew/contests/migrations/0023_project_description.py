# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0022_project_project_submission_project_submission_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='empty'),
            preserve_default=False,
        ),
    ]
