# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-22 11:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contests', '0066_auto_20171122_0902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Points_Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('points', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.Bid_Point')),
            ],
        ),
    ]
