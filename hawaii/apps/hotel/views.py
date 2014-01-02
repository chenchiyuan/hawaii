# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.views.generic import View
from hawaii.apps.hotel.models import Hotel
from libs.http import json_response


class HotelDetailView(View):
    def dispatch(self, request, *args, **kwargs):
        return super(HotelDetailView, self).dispatch(request, *args, **kwargs)

    def get(self, requests, *args, **kwargs):
        hotel = Hotel.objects.get(**kwargs)
        return json_response(hotel.to_json())