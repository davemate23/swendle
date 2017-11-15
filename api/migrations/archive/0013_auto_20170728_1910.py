# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 19:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20170728_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fact',
            name='approval',
        ),
        migrations.AlterField(
            model_name='fact',
            name='upvoted_by',
            field=models.ManyToManyField(null=True, related_name='fact_upv_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
