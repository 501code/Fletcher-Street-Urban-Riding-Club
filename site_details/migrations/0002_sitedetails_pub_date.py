# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-31 06:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitedetails',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
