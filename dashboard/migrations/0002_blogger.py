# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-24 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogger_fn', models.CharField(max_length=255)),
                ('blogger_mn', models.CharField(blank=True, max_length=255, null=True)),
                ('blogger_ln', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
