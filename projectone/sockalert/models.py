# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

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


