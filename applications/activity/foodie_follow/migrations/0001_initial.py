# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 04:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodieFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Modified')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foodie_followers', to=settings.AUTH_USER_MODEL, verbose_name='Follower')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foodie_followings', to=settings.AUTH_USER_MODEL, verbose_name='Following')),
            ],
            options={
                'verbose_name': 'Foodies Follow',
                'verbose_name_plural': 'Foodies Follow',
            },
            bases=(save_the_change.mixins.SaveTheChange, models.Model),
        ),
    ]
