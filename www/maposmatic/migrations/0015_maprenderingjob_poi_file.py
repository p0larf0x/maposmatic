# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-09 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maposmatic', '0014_auto_20180318_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='maprenderingjob',
            name='poi_file',
            field=models.FileField(blank=True, null=True, upload_to='upload/poi/%Y/%m/%d/'),
        ),
    ]
