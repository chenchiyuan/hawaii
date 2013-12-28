# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View
from libs.http import json_response
from hawaii.apps.hotel.models import HotelProduct
from hawaii.apps.commodity.models import CommodityProduct


class SearchProductsView(TemplateView):
    template_name = "search_combine.html"


class SearchFormView(TemplateView):
    template_name = "search_form.html"


class SearchQueryView(View):
    def get(self, request, *args, **kwargs):
        routes = [
            {
                "number": "CA123",
                "inventory_type": u"经济舱",
                "price": "1500",
                "flights": [
                    {
                        "departure": "12:20",
                        "arrival": "12:40",
                        "from_city": "北京",
                        "to_city": "上海",
                        "company": "夏威夷航空",
                        "number": "CA123"
                    },
                    {
                        "departure": "12:20",
                        "arrival": "12:40",
                        "from_city": "北京",
                        "to_city": "上海",
                        "company": "夏威夷航空",
                        "number": "CA123"
                    }
                ],
            },
            {
                "number": "XX345",
                "inventory_type": u"商务舱",
                "price": "1500",
                "flights": [
                    {
                        "departure": "12:20",
                        "arrival": "12:40",
                        "from_city": "北京",
                        "to_city": "上海",
                        "company": "夏威夷航空",
                        "number": "CA123"
                    },
                ],
            }
        ]
        hotels = map(lambda hotel: hotel.to_json(), list(HotelProduct.objects.all()))
        commodities = map(lambda commodity: commodity.to_json(), list(CommodityProduct.objects.all()))
        return json_response({
            "hotels": hotels,
            "commodities": commodities,
            "routes": routes
        })

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SearchQueryView, self).dispatch(request, *args, **kwargs)