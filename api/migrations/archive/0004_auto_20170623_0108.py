# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-23 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170623_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.CharField(max_length=5000),
        ),
    ]
