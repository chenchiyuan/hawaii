# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from hawaii.apps.weixin.views import WeiXinResponseView

urlpatterns = patterns('',
    url(r'^callback/$', WeiXinResponseView.as_view(), name="weixin_response_view"),
)
