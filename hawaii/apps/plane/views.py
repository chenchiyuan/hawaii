# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from libs.emails import send_email
from models import Flight
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
        inventory = Flight.objects.get(id=kwargs.get("id", ""))
        #send_email("zoneke.ccy@gmail.com", "chenchiyuan03@gmail.com", subject=u"新订单",
        #           html="%s %s %s" %(username, phone, inventory))
        return render_to_response("plane/success.html")


class PlaneFormView(TemplateView):
    template_name = "plane/form.html"


class PlaneSearchView(TemplateView):
    template_name = "plane/search.html"

    def get_context_data(self, **kwargs):
        context = super(PlaneSearchView, self).get_context_data(**kwargs)
        context['flights'] = self.get_flights()
        return context

    def get_flights(self):
        starting = self.request.GET.get("starting", "")
        destination = self.request.GET.get("destination", "")
        try:
            departure = datetimes.str_to_datetime(self.request.GET.get("departure", ""), datetimes.DATE_FORMAT)
        except Exception, err:
            return []

        ending = datetimes.datetime_delta(departure, days=1)

        if not all([starting, departure, destination]):
            return []

        flights = Flight.objects.filter(
            starting=starting,
            destination=destination,
            departure__gte=departure,
            departure__lte=ending)
        return flights

