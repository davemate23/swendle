# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 00:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='wrong_cluster',
            field=models.ManyToManyField(related_name='wrong_cluster', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='wrong_story',
            field=models.ManyToManyField(related_name='wrong_story', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
