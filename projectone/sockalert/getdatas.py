# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import yx_api, yx_sp
from django.http import HttpResponse
import time
# Create your tests here.


def select_all(request):
    list = yx_api.objects.all()
    response = ''
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = yx_api.objects.filter(id=1)
    # 获取单个对象
    # response3 = yx_api.objects.get(id=1)
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # yx_api.objects.order_by('url')[0:2]
    # 数据排序
    # yx_api.objects.order_by("id")
    # 上面的方法可以连锁使用
    # yx_api.objects.filter(url='https://a.com').order_by("id")
    for var in list:
        response += unicode(var.id) + unicode(', ') + var.url + ' ' + '<br>'
    response = response
    return HttpResponse('<p>' + response + '</p>')


def save_data(request):
    newdata = yx_api(id=5, url='https://e.com', crttime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    newdata.save()
    return HttpResponse('<p>数据添加成功</p>')


def del_data(request):
    # 删除id=1的数据
    pre_del = yx_api.objects.get(id=1)
    pre_del.delete()
    # 另外一种方式
    # yx_api.objects.filter(id=1).delete()
    # 删除所有数据
    # yx_api.objects.all().delete()
    return HttpResponse("<p>删除成功</p>")