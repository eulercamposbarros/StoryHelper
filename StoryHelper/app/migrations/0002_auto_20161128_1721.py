# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 19:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='comentario',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 28, 17, 21, 34, 934093)),
        ),
        migrations.AlterField(
            model_name='writer',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='nome',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
