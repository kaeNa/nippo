# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-22 07:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0006_auto_20160822_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='contributor',
            new_name='user',
        ),
    ]
