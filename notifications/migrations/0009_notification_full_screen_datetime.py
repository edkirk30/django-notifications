# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-05 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0008_auto_20180601_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='full_screen_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
