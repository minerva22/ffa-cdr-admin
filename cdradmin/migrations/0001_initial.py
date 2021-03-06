# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-17 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Liability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=255)),
                ('long_description', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=255)),
                ('long_description', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Superid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('superid', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SuperidToLoanLiability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guarantee', models.IntegerField(default=0)),
                ('maturity_date', models.DateField(null=True)),
                ('ledger', models.CharField(max_length=255)),
                ('closed', models.BooleanField(default=False)),
                ('country_of_utilization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdradmin.Country')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdradmin.Currency')),
                ('liability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdradmin.Liability')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdradmin.Loan')),
                ('superid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdradmin.Superid')),
            ],
        ),
    ]
