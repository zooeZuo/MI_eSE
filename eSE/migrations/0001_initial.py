# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-09 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='restrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apduModelList', models.CharField(max_length=10000)),
                ('apduResultList', models.CharField(max_length=10000)),
                ('scriptsInstanceId', models.CharField(max_length=100)),
                ('xmTransTime', models.CharField(max_length=40)),
                ('xmTransNum', models.CharField(max_length=40)),
                ('spTransTime', models.CharField(max_length=40)),
                ('spTransNum', models.CharField(max_length=40)),
            ],
        ),
    ]