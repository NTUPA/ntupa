# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equip', '0005_auto_20160702_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='', max_length=100, verbose_name='活動地點'),
            preserve_default=False,
        ),
    ]