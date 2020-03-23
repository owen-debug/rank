#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 18:24
# @Author  : Ryu
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path, re_path

from gamerank import views

urlpatterns = [
    path('uprank/', views.upranka),
    re_path(r'getquery/(\d+)/(\d+)', views.get_query)
]
