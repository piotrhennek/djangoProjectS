# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20171205_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templates',
            name='text',
            field=models.TextField(),
        ),
    ]
