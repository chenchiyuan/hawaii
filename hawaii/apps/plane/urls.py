# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, include, url
from views import PlaneSearchView

urlpatterns = patterns('',
    url(r'^search/', PlaneSearchView.as_view(), name="plane_search_view"),
)
