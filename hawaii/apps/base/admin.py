# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.contrib import admin
from models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'show_from', 'show_to', 'priority']
    search_fields = ['code', 'name']
    list_filter = ['show_from', 'show_to']

admin.site.register(City, CityAdmin)