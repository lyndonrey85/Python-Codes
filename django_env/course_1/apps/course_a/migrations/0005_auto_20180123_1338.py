# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-23 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_a', '0004_auto_20180123_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='user_favorites',
            field=models.ManyToManyField(related_name='favorites', to='login.User'),
        ),
    ]
