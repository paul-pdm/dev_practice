# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-07 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_auto_20161207_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='url',
        ),
        migrations.AddField(
            model_name='page',
            name='note',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]