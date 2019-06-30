# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': '공지사항',
                'verbose_name_plural': '공지사항 목록',
                'ordering': ('-created_date',),
            },
        ),
    ]