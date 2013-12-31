# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View
from libs.emails import send_email
from libs.http import json_response
from hawaii.apps.hotel.models import HotelProduct
from hawaii.apps.commodity.models import CommodityProduct
from hawaii.apps.plane.services import Route, City
import json


class ConfirmProductsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ConfirmProductsView, self).dispatch(request, *args, **kwargs)

    def post(self, requests, *args, **kwargs):
        products_json_data = json.loads(requests.body)
        html = self.get_html(**products_json_data)
        send_email("chenchiyuan03@gmail.com;kent03@163.com", subject=u"新订单", html=html)
        return json_response({"status": 200})

    def routes(self, routes):
        contents = []
        for route in routes:
            number = route.get("number", "")
            company = route.get("company", "")
            departure = route.get("departure", "")
            arrival = route.get("arrival", "")
            starting = route.get("starting", "")
            destination = route.get("destination", "")
            content = "航空公司: %s, 航班号: %s, 出发时间: %s, 抵达时间: %s, 出发地: %s, 抵达地: %s"\
                      % (company, number, departure, arrival, starting, destination)
            contents.append(content)
        return "</br>".join(contents)

    def hotels(self, hotels):
        pass

    def commodities(self, commodities):
        pass

    def users(self, users):
        contents = []
        for user in users:
            username = user.get("firstname", "") + user.get("secondname", "")
            birthday = user.get("birthday", "")
            identify = user.get("identify", "")
            country = user.get("country", "")
            content = "用户名: %s, 生日: %s, 身份证: %s, 国籍: %s" % (username, birthday, identify, country)
            contents.append(content)
        return "</br>".join(contents)

    def get_html(self, phone="", users=[], products=[], **kwargs):
        html = []
        phone_html = "手机号: %s" % phone
        users_html = self.users(users)
        routes_html = self.routes(products.get("routes", []))
        html.extend([phone_html, users_html, routes_html])
        return "</br>".join(html)

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