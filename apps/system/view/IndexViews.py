# -*- coding: UTF-8 -*-
"""
   #前台主页信息入口
"""
from django.shortcuts import render


def to_system(request):
    return render(request, 'sys_base.html')
