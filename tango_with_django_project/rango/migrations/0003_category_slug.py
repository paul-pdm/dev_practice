# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20161127_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]