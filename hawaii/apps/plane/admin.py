# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from models import Flight, FlightInventory, FlightPrivilege, Day, FlightProduct
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
    filter_horizontal = ("days", )
    raw_id_fields = ("flight", )

    list_display = ("seat", "inventory_type", "begin", "end", "show_days", "price", "child_price")

    def show_days(self, obj):
        days = obj.days.all().values_list("name", flat=True)
        return ";".join(days)

    show_days.short_description = u"有效日"


class FlightAdmin(admin.ModelAdmin):
    inlines = [
        FlightInventoryInline,
        FlightPrivilegeInline,
    ]


class FlightProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Flight, FlightAdmin)
admin.site.register(FlightInventory, FlightInventoryAdmin)
admin.site.register(FlightPrivilege, FlightPrivilegeAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(FlightProduct, FlightProductAdmin)