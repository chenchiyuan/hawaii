# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.views.generic import TemplateView
from models import PlaneInventory
from libs import datetimes


class PlaneFormView(TemplateView):
    template_name = "plane/form.html"


class PlaneSearchView(TemplateView):
    template_name = "plane/search.html"

    def get_context_data(self, **kwargs):
        context = super(PlaneSearchView, self).get_context_data(**kwargs)
        context['planes'] = self.get_planes()
        return context

    def get_planes(self):
        starting = self.request.GET.get("starting", "")
        destination = self.request.GET.get("destination", "")
        try:
            departure = datetimes.str_to_datetime(self.request.GET.get("departure", ""), datetimes.DATE_FORMAT)
        except Exception, err:
            return []

        ending = datetimes.datetime_delta(departure, days=1)

        if not all([starting, departure, destination]):
            return []

        planes = PlaneInventory.objects.filter(
            starting=starting,
            destination=destination,
            departure__gte=departure,
            departure__lte=ending)
        return planes