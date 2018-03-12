# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(yx_api)
class disp(admin.ModelAdmin):
    list_display = ('id', 'url', 'data', 'crttime')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)   # -id
    # list_editable 设置默认可编辑字段
    list_editable = ['data']


@admin.register(yx_sp)
class disp(admin.ModelAdmin):
    list_display = ('id', 'url', 'data', 'crttime')
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  # -id
    # list_editable 设置默认可编辑字段
    list_editable = ['data']


