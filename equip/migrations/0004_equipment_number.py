# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equip', '0003_equipment_belongs_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='number',
            field=models.IntegerField(default=0, verbose_name='編號'),
        ),
    ]