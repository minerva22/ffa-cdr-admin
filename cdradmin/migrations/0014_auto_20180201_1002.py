# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-01 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cdradmin', '0013_superidtoloanliability_subledger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superidtoloanliability',
            name='ledger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdradmin.Ledger'),
        ),
    ]
