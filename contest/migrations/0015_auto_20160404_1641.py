# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-04 08:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0014_auto_20160404_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contestproblem',
            old_name='spj_code_language',
            new_name='spj_language',
        ),
    ]
