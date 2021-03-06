# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='null', max_length=45),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='null', max_length=45),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(default='null', max_length=45),
        ),
    ]
