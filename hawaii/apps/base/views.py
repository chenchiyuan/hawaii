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
from libs.datetimes import str_to_datetime, datetime_delta, DATE_FORMAT
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

    def get_html(self, phone="", users=[], products={}, **kwargs):
        html = []
        contact = kwargs.get("contact", "")
        email = kwargs.get("email", "")
        user_count = kwargs.get("user_count", "")
        contact_html = "联系人: %s, 手机号: %s, 邮箱: %s, 出行人数: %s" % (contact, phone, email, user_count)
        users_html = self.users(users)
        routes_html = self.routes(products.get("routes", []))
        html.extend([contact_html, users_html, routes_html])
        return "</br>".join(html)

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
                                                          check_in_time__lt=departure_tomorrow)))
            commodities = map(lambda commodity: commodity.to_json(),
                              list(CommodityProduct.objects.filter(city=city,
                                                                   datetime__gte=departure,
                                                                   datetime__lt=departure_tomorrow)))
        routes = map(lambda route: route.to_json(), routes_search)

        def cmp(a, b):
            price_a = int(a['price']) + int(a['tax'])
            price_b = int(b['price']) + int(b['tax'])
            if price_a <= price_b:
                return -1
            else:
                return 1
        routes = sorted(routes, cmp=cmp)

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