# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-22 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=45)),
                ('alias', models.CharField(default='', max_length=45)),
                ('email', models.CharField(default='', max_length=45)),
                ('password', models.CharField(default='', max_length=200)),
            ],
        ),
    ]