# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, url
from hawaii.apps.base.views import SearchFormView, SearchQueryView, SearchProductsView


urlpatterns = patterns('',
    url(r'^form/$', SearchFormView.as_view(), name="base_form_view"),
    url(r'^products/$', SearchProductsView.as_view(), name="base_products_view"),
    url(r'^search/$', SearchQueryView.as_view(), name="base_search_view"),
)
