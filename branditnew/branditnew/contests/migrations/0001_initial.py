# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 13:38
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('prize_lower_limit', models.PositiveSmallIntegerField()),
                ('parent_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('prize', models.PositiveIntegerField()),
                ('end_date', models.DateField()),
                ('is_paid_for', models.BooleanField(default=False)),
                ('is_top', models.BooleanField(default=False)),
                ('is_hidden', models.BooleanField(default=False)),
                ('is_nda', models.BooleanField(default=False)),
                ('is_sealed', models.BooleanField(default=False)),
                ('cost', models.PositiveSmallIntegerField()),
                ('files', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.Category')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[['admin', 'Administrator'], ['client', 'Client'], ['bl', 'Brandlancer']], default='client', max_length=6)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('activation_key', models.CharField(max_length=50)),
                ('is_activated', models.BooleanField(default=False)),
                ('points', models.DecimalField(decimal_places=0, max_digits=10000)),
                ('profile_image', models.FileField(upload_to='uploads/profile_images/%Y/%m/%d')),
                ('address', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('how_found_us', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[['php', 'PHP'], ['css', 'CSS'], ['html', 'HTML'], ['photoshop', 'Photoshop'], ['coralDraw', 'Coral Draw']], max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contests.Skills'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
