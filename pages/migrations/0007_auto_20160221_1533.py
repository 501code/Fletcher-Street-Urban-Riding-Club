# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20160221_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(default='none.jpg', upload_to='uploads/'),
        ),
    ]
