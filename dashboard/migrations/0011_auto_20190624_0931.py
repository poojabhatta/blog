# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-24 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20190624_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]