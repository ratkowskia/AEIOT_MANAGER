# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-04 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aeiot', '0003_auto_20160926_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algorithm',
            name='source_code',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
