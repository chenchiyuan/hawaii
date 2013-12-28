# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View
from libs.http import json_response
from hawaii.apps.hotel.models import HotelProduct
from hawaii.apps.commodity.models import CommodityProduct
from hawaii.apps.plane.services import Route, City


class SearchProductsView(TemplateView):
    template_name = "search_combine.html"


class SearchFormView(TemplateView):
    template_name = "search_form.html"


class SearchQueryView(View):
    def get(self, request, *args, **kwargs):
        page_size = 3

        query_dict = self.get_route_query_dict(request, *args, **kwargs)
        city = City.get_name(query_dict.get("destination", ""))
        routes_search = Route.search(**query_dict)
        if not city:
            hotels = []
            commodities = []
        else:
            hotels = map(lambda hotel: hotel.to_json(),
                         list(HotelProduct.objects.filter(city=city)))
            commodities = map(lambda commodity: commodity.to_json(),
                              list(CommodityProduct.objects.filter(city=city)))
        routes = map(lambda route: route.to_json(), routes_search)
        return json_response({
            "hotels": hotels[:page_size],
            "commodities": commodities[:page_size],
            "routes": routes[:page_size]
        })

    def get_route_query_dict(self, request, *args, **kwargs):
        starting = request.GET.get("starting", "")
        destination = request.GET.get("destination", "")
        departure = request.GET.get("departure", "")
        back_time = request.GET.get("back_time", "")
        seat_type = request.GET.get("seat_type", "")
        amount = request.GET.get("amount", 1)
        query_dict = {
            "starting": starting,
            "destination": destination,
            "departure": departure,
            "back_time": back_time,
            "seat_type": seat_type,
            "amount": amount
        }
        return query_dict


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SearchQueryView, self).dispatch(request, *args, **kwargs)