# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-06 12:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='string',
            new_name='Searchdata',
        ),
    ]
