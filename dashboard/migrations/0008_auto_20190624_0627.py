# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-24 06:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20190624_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
