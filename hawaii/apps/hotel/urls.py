# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from hawaii.apps.hotel.views import HotelDetailView
from hawaii import const

urlpatterns = patterns('',
    url(r'^%s/$' % const.URL_ID, HotelDetailView.as_view(), name="hotel_detail_view"),
)
