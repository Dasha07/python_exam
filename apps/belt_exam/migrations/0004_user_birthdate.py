# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-24 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('belt_exam', '0003_auto_20170324_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]