# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 09:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodlands', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='detailed_describtion',
            new_name='detailed_description',
        ),
    ]
