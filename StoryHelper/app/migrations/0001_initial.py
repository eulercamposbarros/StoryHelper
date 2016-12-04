# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 01:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avalicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coerencia', models.IntegerField()),
                ('diversao', models.IntegerField()),
                ('data', models.DateTimeField(default=datetime.datetime(2016, 12, 6, 23, 25, 39, 816562))),
                ('comentario', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=1024)),
                ('estilo', models.CharField(max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('criado_pelo_usuario', models.BooleanField(default=True)),
                ('ordem', models.IntegerField()),
                ('historia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Historia')),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.TextField()),
                ('next_sentence', models.TextField()),
                ('keys', models.CharField(max_length=1024, null=True)),
                ('sujeito', models.CharField(max_length=1024, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='avalicao',
            name='historia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Historia'),
        ),
    ]
