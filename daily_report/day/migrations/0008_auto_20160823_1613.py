# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-23 07:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0007_auto_20160822_1625'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Report',
        ),
        migrations.RenameField(
            model_name='impression',
            old_name='book',
            new_name='report',
        ),
    ]