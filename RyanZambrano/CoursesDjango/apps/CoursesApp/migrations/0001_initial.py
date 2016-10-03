# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
