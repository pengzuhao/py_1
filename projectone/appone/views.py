# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from appone import models
from django.shortcuts import render,HttpResponse


# def ind(request):
#     return render(request, "ind.html")


def index(request):
    if request.method == 'POST':
        username =  request.POST.get('username', None)
        password = request.POST.get('password', None)
        models.UserInfo.objects.create(user=username, pwd=password)
    userlist = models.UserInfo.objects.all()
    return render(request, "index.html", {"data": userlist})
