# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
import save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedialLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Modified')),
                ('title', models.CharField(choices=[(b'facebook', 'Facebook'), (b'twitter', 'Twitter'), (b'google', 'Google+'), (b'instagram', 'Instagram'), (b'linkedin', 'Linkedin'), (b'youtube', 'Youtube'), (b'pinterest', 'Pinterest')], max_length=150, verbose_name='Title')),
                ('link', models.CharField(max_length=300, verbose_name='Link')),
                ('targt', models.CharField(choices=[(b'_blank', b'Blank'), (b'_top', b'Top')], default=b'_blank', max_length=6, verbose_name='Target')),
                ('sort_order', models.IntegerField(default=0, verbose_name='Sort order')),
                ('display', models.BooleanField(default=True, verbose_name='Publish')),
            ],
            options={
                'ordering': ('sort_order',),
                'verbose_name': 'Social Media Link',
                'verbose_name_plural': 'Social Media Links',
            },
            bases=(save_the_change.mixins.SaveTheChange, models.Model),
        ),
    ]