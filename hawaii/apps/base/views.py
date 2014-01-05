# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View
from libs.emails import send_email
from libs.http import json_response
from hawaii.apps.hotel.models import HotelProduct
from hawaii.apps.commodity.models import CommodityProduct
from hawaii.apps.plane.services import Route, City, Flight
from libs.datetimes import str_to_datetime, datetime_delta, DATE_FORMAT, now
from django.conf import settings
import json
import const


class ConfirmProductsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ConfirmProductsView, self).dispatch(request, *args, **kwargs)

    def post(self, requests, *args, **kwargs):
        products_json_data = json.loads(requests.body)
        html = self.get_html(**products_json_data)
        if not settings.DEBUG:
            send_email(settings.EMAIL_TO, subject=const.get_email_title(), html=html)
        return json_response({"status": 200})

    def get_html(self, **kwargs):
        user_type_mapping = {
            "adult": u"成人",
            "child": u"儿童"
        }
        for user in kwargs.get("users", []):
            user['user_type'] = user_type_mapping.get(user.get('user_type', ""), u"成人")

        routes = kwargs['products'].get("routes", [])
        for route in routes:
            route['limits'] = Route.get_limits(route['limit_no'])
            for flight in route.get("flights", []):
                flight['seat_type'] = Flight.get_type(seat_type=flight.get("seat_type", ""))
                flight['departure'] = Flight.format_datetime(flight['departure'])
                flight['arrival'] = Flight.format_datetime(flight['arrival'])

        pnr = self.get_pnr(routes)
        const_data = self.get_const()
        kwargs.update(const_data)
        kwargs['pnr'] = pnr
        return render_to_string("email.html", kwargs)

    def get_pnr(self, routes):
        print(routes)
        return "PNR123"

    def get_const(self):
        return {
            "company_logo": "http://www.hawaiianairlines.com.cn/app_themes/hawaiianair.cn_dev/img/header/logo.png",
            "company_phone": "010-85227835",
            "datetime": now(),
        }

class SearchProductsView(TemplateView):
    template_name = "search_combine.html"


class SearchFormView(TemplateView):
    template_name = "search_form.html"


class SearchQueryView(View):
    def get(self, request, *args, **kwargs):
        page_size = 5

        query_dict = self.get_route_query_dict(request, *args, **kwargs)
        city = City.get_name(query_dict.get("destination", ""))
        routes_search = Route.search(**query_dict)
        departure = str_to_datetime(query_dict.get("departure", ""), DATE_FORMAT)
        departure_tomorrow = datetime_delta(departure, days=1)

        if not city:
            hotels = []
            commodities = []
        else:
            hotels = map(lambda hotel: hotel.to_json(),
                         list(HotelProduct.objects.filter(city=city,
                                                          check_in_time__gte=departure,
                                                          check_in_time__lt=departure_tomorrow).select_related()))
            commodities = map(lambda commodity: commodity.to_json(),
                              list(CommodityProduct.objects.filter(city=city,
                                                                   datetime__gte=departure,
                                                                   datetime__lt=departure_tomorrow).select_related()))
        routes = map(lambda route: route.to_json(), routes_search)

        def cmp(a, b):
            price_a = int(a['price']) + int(a['tax'])
            price_b = int(b['price']) + int(b['tax'])
            if price_a <= price_b:
                return -1
            else:
                return 1
        routes = sorted(routes, cmp=cmp)

        routes_available = ['HA', 'KE']
        #routes = filter(lambda route: route['company_three'] in routes_available, routes)

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