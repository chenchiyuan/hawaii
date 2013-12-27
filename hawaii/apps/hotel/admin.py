# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from models import Hotel, HotelInventory, HotelDay, HotelPrivilege, HotelProduct
from django.contrib import admin


class HotelDayAdmin(admin.ModelAdmin):
    pass


class HotelPrivilegeAdmin(admin.ModelAdmin):
    pass


class HotelInventoryAdmin(admin.ModelAdmin):
    filter_horizontal = ("days", )
    raw_id_fields = ("hotel", )

    list_display = ("amount", "inventory_type", "begin", "end", "show_days", "price")

    def show_days(self, obj):
        days = obj.days.all().values_list("name", flat=True)
        return ";".join(days)

    show_days.short_description = u"有效日"


class HotelAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/static/css/admin-override.css", ),
        }


class HotelProductAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "amount", "price", "inventory_type", "remark")


admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelInventory, HotelInventoryAdmin)
admin.site.register(HotelProduct, HotelProductAdmin)
admin.site.register(HotelDay, HotelDayAdmin)