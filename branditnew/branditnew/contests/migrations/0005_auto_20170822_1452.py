# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0004_profile_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='date_of_birth',
            new_name='birth_date',
        ),
    ]
