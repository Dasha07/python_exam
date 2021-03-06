# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-24 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_exam', '0006_auto_20170324_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='author',
            name='creater',
        ),
        migrations.RemoveField(
            model_name='author',
            name='quote',
        ),
        migrations.AddField(
            model_name='quote',
            name='posted_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='all_quotes', to='belt_exam.User'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.AddField(
            model_name='favorite',
            name='quote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quote_favorites', to='belt_exam.Quote'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favorites', to='belt_exam.User'),
        ),
    ]
