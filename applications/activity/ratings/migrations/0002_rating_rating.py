# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='rating',
            field=models.PositiveIntegerField(default=1, verbose_name='Rating'),
            preserve_default=False,
        ),
    ]