# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20170728_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='citation',
            name='approval',
            field=models.BooleanField(default=True),
        ),
    ]
