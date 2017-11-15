# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-04 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20170627_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='story',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]