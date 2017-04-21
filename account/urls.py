__author__ = 'qiqi'
# -*- coding: UTF-8 -*-
from django.conf.urls import url
from account.views import user_login, dashboard
from django.contrib.auth.views import login, logout, logout_then_login

urlpatterns = [
    # url(r'^login/$', user_login, name='login'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^$', dashboard, name='dashboard'),
]
