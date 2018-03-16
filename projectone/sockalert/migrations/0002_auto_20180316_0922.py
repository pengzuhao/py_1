# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-16 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sockalert', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mailusers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=255, verbose_name='MailAddr')),
                ('status', models.CharField(max_length=20, verbose_name='Status')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='mailusers',
            unique_together=set([('mail',)]),
        ),
    ]
