# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-27 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_device_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='firebase_token',
            field=models.CharField(max_length=200),
        ),
    ]
