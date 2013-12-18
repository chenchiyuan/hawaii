# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.views.generic import TemplateView


class PlaneSearchView(TemplateView):
    template_name = "plane/search.html"