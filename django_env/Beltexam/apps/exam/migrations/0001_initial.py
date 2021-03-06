# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-30 21:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='friends_added', to='login.User')),
                ('other_users', models.ManyToManyField(related_name='other_user', to='login.User')),
            ],
        ),
    ]
