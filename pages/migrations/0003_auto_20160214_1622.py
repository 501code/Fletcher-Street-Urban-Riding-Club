# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_section_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='order',
            field=models.IntegerField(default=100),
        ),
    ]
