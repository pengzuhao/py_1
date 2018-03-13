# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import yx_api, yx_sp
from django.http import HttpResponse
# Create your tests here.


def select_all(request):
    list = yx_api.objects.all()
    response = ''
    for var in list:
        response += unicode(var.id) + unicode(', ') + var.url + ' ' + '<br>'
    response = response
    return HttpResponse('<p>' + response + '</p>')





