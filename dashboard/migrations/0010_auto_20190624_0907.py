# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-24 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_comment_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.ImageField(blank=True, default='static/frontend/images/download.jpeg', null=True, upload_to=''),
        ),
    ]
