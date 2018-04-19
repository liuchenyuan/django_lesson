#!/usr/bin/env python
# -+- coding:utf-8 -+-
# @Time     :2018/4/9 14:08
# @Author   :lcy
# @File     :urls.py

from django.conf.urls import url

from blog.views import index, article_year, register, login

urlpatterns = [
    url(r'^index', index),
    url(r'^register', register, name='reg'),
    url(r'^(?P<year>\d{4})/(?P<mon>\d{2})$', article_year),
    url(r'^login', login)

]