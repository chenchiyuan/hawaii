# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^callback/$', PlaneFormView.as_view(), name="plane_form_view"),
)
