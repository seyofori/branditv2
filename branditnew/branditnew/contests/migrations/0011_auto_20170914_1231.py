# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0010_auto_20170830_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='design_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='contest',
            name='preferred_colors',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='preferred_style',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='sketch',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='contest',
            name='target_audience',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='would_like_to_print',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
