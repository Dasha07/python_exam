# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-24 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_exam', '0005_quote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='belt_exam.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='quote',
            name='author',
        ),
        migrations.AddField(
            model_name='author',
            name='quote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='belt_exam.Quote'),
        ),
    ]
