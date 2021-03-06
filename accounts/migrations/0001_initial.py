# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 11:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, unique=True)),
                ('name', models.CharField(max_length=80)),
                ('desc', models.TextField(blank=True)),
                ('address_one', models.CharField(max_length=100)),
                ('address_two', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('phone', models.CharField(max_length=10)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'accounts',
            },
        ),
    ]
