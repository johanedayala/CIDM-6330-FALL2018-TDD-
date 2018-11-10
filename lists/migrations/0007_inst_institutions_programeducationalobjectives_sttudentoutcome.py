# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-09 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_item_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField()),
                ('password', models.TextField()),
                ('confirm_password', models.TextField()),
                ('name', models.TextField()),
                ('street', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('zipcode', models.TextField()),
                ('mission', models.TextField()),
                ('list', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lists.List')),
            ],
        ),
        migrations.CreateModel(
            name='Institutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='programEducationalObjectives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.TextField()),
                ('objective', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='sttudentOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.TextField()),
                ('sttudentOutcome', models.TextField()),
            ],
        ),
    ]
