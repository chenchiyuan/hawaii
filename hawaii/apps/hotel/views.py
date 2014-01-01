# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.views.generic import View
from libs.http import json_response


class HotelDetailView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(HotelDetailView, self).dispatch(request, *args, **kwargs)

    def get(self, requests, *args, **kwargs):
        return json_response