# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-19 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdradmin', '0010_auto_20180118_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='superidtoloanliability',
            name='guarantee_type',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
