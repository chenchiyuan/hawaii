# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from models import Commodity, CommodityDay, CommodityInventory, CommodityProduct
from django.contrib import admin


class CommodityDayAdmin(admin.ModelAdmin):
    pass


class CommodityPrivilegeAdmin(admin.ModelAdmin):
    pass


class CommodityInventoryAdmin(admin.ModelAdmin):
    filter_horizontal = ("days", )
    raw_id_fields = ("commodity", )

    list_display = ("amount", "inventory_type", "begin", "end", "show_days", "price")

    def show_days(self, obj):
        days = obj.days.all().values_list("name", flat=True)
        return ";".join(days)

    show_days.short_description = u"有效日"


class CommodityAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/static/css/admin-override.css", ),
        }


class CommodityProductAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "amount", "price", "inventory_type", "remark")


admin.site.register(Commodity, CommodityAdmin)
admin.site.register(CommodityInventory, CommodityInventoryAdmin)
admin.site.register(CommodityProduct, CommodityProductAdmin)
admin.site.register(CommodityDay, CommodityDayAdmin)