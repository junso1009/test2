# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-22 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create Date'),
        ),
    ]
