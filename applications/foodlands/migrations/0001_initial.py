# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 13:41
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foodland_specifications', '0001_initial'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Modified')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=255, populate_from=b'name', unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('location_note', models.TextField(blank=True, max_length=1000, null=True)),
                ('lat', models.CharField(blank=True, max_length=100, null=True, verbose_name='Latitude')),
                ('lng', models.CharField(blank=True, max_length=100, null=True, verbose_name='Longitude')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('small_description', models.TextField(blank=True, null=True, verbose_name='Small Description')),
                ('detailed_describtion', ckeditor.fields.RichTextField(blank=True, help_text='Detailed Description', null=True)),
                ('restaurant_type', models.CharField(choices=[(b'v', 'VEG'), (b'n', 'NON-VEG')], default=b'n', max_length=1, verbose_name='Restaurant Type')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='Main Image ')),
                ('open_time', models.TimeField(blank=True, null=True, verbose_name='Open time')),
                ('close_time', models.TimeField(blank=True, null=True, verbose_name='Close time')),
                ('average_cost', models.IntegerField(blank=True, null=True, verbose_name='Average cost')),
                ('search_tags', models.TextField(blank=True, null=True, verbose_name='Search Tags')),
                ('published', models.BooleanField(default=False, verbose_name='Published?')),
                ('foodlands_food_rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Food')),
                ('foodlands_ambiance_rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Ambiance')),
                ('foodlands_service_rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Service')),
                ('dishes_count', models.IntegerField(default=0, verbose_name='Dishes Count')),
                ('favourite_count', models.IntegerField(default=0, verbose_name='Favourite Count')),
                ('follow_count', models.IntegerField(default=0, verbose_name='Follow Count')),
                ('recommend_count', models.IntegerField(default=0, verbose_name='Recommends Count')),
                ('review_count', models.IntegerField(default=0, verbose_name='Review Count')),
                ('check_in_count', models.IntegerField(default=0, verbose_name='Check in Count')),
                ('user_food_rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='User food rating')),
                ('user_ambiance_rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='User amb rating')),
                ('user_service_rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='User service rating')),
                ('seo_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('seo_description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('seo_keywords', models.TextField(blank=True, null=True, verbose_name='Keywords')),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='SEO Image')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.City', verbose_name='City')),
                ('cuisines', models.ManyToManyField(blank=True, to='foodland_specifications.Cuisine')),
                ('highlights', models.ManyToManyField(blank=True, related_name='get_highlights', to='foodland_specifications.HighLight')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.Place', verbose_name='Place')),
                ('serves', models.ManyToManyField(blank=True, to='foodland_specifications.Serve')),
                ('similar_restaurants', models.ManyToManyField(blank=True, related_name='_restaurant_similar_restaurants_+', to='foodlands.Restaurant')),
                ('suitable', models.ManyToManyField(blank=True, to='foodland_specifications.Suitable')),
            ],
            options={
                'verbose_name': 'Foodland',
                'verbose_name_plural': 'Foodlands',
            },
            bases=(save_the_change.mixins.SaveTheChange, models.Model),
        ),
    ]
