# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from models import Flight, FlightInventory, FlightPrivilege, Day
from django.contrib import admin


class DayAdmin(admin.ModelAdmin):
    pass


class FlightInventoryInline(admin.StackedInline):
    model = FlightInventory
    extra = 1


class FlightPrivilegeInline(admin.StackedInline):
    model = FlightPrivilege
    extra = 1


class FlightPrivilegeAdmin(admin.ModelAdmin):
    pass


class FlightInventoryAdmin(admin.ModelAdmin):
    #filter_horizontal = ("days", )
    pass

class FlightAdmin(admin.ModelAdmin):
    inlines = [
        FlightInventoryInline,
        FlightPrivilegeInline,
    ]


admin.site.register(Flight, FlightAdmin)
admin.site.register(FlightInventory, FlightPrivilegeAdmin)
admin.site.register(FlightPrivilege, FlightInventoryAdmin)
admin.site.register(Day, DayAdmin)