# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
