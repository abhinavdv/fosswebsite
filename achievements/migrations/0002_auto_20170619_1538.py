# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intern',
            old_name='data',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='contest',
            name='contest_id',
            field=models.CharField(max_length=200),
        ),
    ]
