# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from libs.emails import send_email
from models import FlightProduct
from libs import datetimes


class PlaneConfirmView(TemplateView):
    template_name = "plane/confirm.html"

    def get_context_data(self, **kwargs):
        context = super(PlaneConfirmView, self).get_context_data(**kwargs)
        inventory = kwargs.get("id", "")
        if not inventory:
            raise Exception()
        context['inventory'] = inventory
        return context

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username", "")
        phone = request.POST.get("phone", "")
        product = FlightProduct.objects.get(id=kwargs.get("id", ""))
        send_email("zoneke.ccy@gmail.com", "chenchiyuan03@gmail.com;kent03@163.com", subject=u"新订单",
                   html="%s %s %s" % (username, phone, product.html))
        return render_to_response("plane/success.html")


class PlaneFormView(TemplateView):
    template_name = "plane/form.html"


class PlaneSearchView(TemplateView):
    template_name = "plane/search.html"

    def get_context_data(self, **kwargs):
        context = super(PlaneSearchView, self).get_context_data(**kwargs)
        context['products'] = self.get_products()
        return context

    def get_products(self):
        starting = self.request.GET.get("starting", "")
        destination = self.request.GET.get("destination", "")
        try:
            departure = datetimes.str_to_datetime(self.request.GET.get("departure", ""), datetimes.DATE_FORMAT)
        except Exception, err:
            return []

        ending = datetimes.datetime_delta(departure, days=1)

        if not all([starting, departure, destination]):
            return []

        products = FlightProduct.objects.filter(
            starting=starting,
            destination=destination,
            departure__gte=departure,
            departure__lte=ending)
        return products

