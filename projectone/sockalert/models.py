# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.utils.html import format_html
# Create your models here.


class yx_api(models.Model):
    id = models.AutoField('ID', primary_key=True, auto_created=True)
    url = models.URLField('URL', max_length=255)
    crttime = models.DateTimeField('CreateTime', auto_now=True)
    data = models.CharField('Data', max_length=255, blank=True)

    class Meta:
        unique_together = ('url',)
        app_label = 'sockalert'


class yx_sp(models.Model):
    id = models.AutoField('ID', primary_key=True, auto_created=True)
    url = models.URLField('URL', max_length=255)
    crttime = models.DateTimeField('CreateTime', auto_now=True)
    data = models.CharField('Data', max_length=255, blank=True)

    class Meta:
        unique_together = ('url',)
        app_label = 'sockalert'


class mailusers(models.Model):
    id = models.AutoField('ID', primary_key=True, auto_created=True)
    mail = models.CharField('MailAddr', max_length=255)
    GENDER_CHOICE = (
        (u'E', u'Enable'),
        (u'D', u'Disable'),
    )
    status = models.CharField('Status', max_length=20, choices=GENDER_CHOICE)

    class Meta:
        unique_together = ('mail',)
        app_label = 'sockalert'