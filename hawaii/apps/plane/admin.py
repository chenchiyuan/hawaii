# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from models import Plane, PlaneInventory
from django.contrib import admin


class PlaneInventoryInline(admin.StackedInline):
    model = PlaneInventory
    extra = 1


class PlaneAdmin(admin.ModelAdmin):
    inlines = [
        PlaneInventoryInline,
    ]

admin.site.register(Plane, PlaneAdmin)
