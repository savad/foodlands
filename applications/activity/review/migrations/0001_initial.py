# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 14:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Modified')),
                ('object_id', models.PositiveIntegerField()),
                ('review_text', models.TextField(blank=True, null=True)),
                ('food_rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Food rating')),
                ('ambiance_rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Ambiance rating')),
                ('service_rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='service rating')),
                ('review_type', models.CharField(choices=[(b'c', 'COMMENT'), (b'rt', 'RATING'), (b'rw', 'REVIEW')], default=b'rw', max_length=2, verbose_name='Review Type')),
                ('expire', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_review_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
            bases=(save_the_change.mixins.SaveTheChange, models.Model),
        ),
    ]
