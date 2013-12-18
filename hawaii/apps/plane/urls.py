# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, include, url
from views import PlaneSearchView, PlaneFormView

urlpatterns = patterns('',
    url(r'^form/', PlaneFormView.as_view(), name="plane_form_view"),
    url(r'^search/', PlaneSearchView.as_view(), name="plane_search_view"),
)
