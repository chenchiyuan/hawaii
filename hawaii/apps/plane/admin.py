# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from models import Plane, PlaneInventory, PlanePrivilege
from django.contrib import admin


class PlaneInventoryInline(admin.StackedInline):
    model = PlaneInventory
    extra = 1


class PlanePrivilegeInline(admin.StackedInline):
    model = PlanePrivilege
    extra = 1


class PlaneInventoryAdmin(admin.ModelAdmin):
    pass


class PlanePrivilegeAdmin(admin.ModelAdmin):
    pass


class PlaneAdmin(admin.ModelAdmin):
    inlines = [
        PlanePrivilegeInline,
        PlaneInventoryInline,
    ]

admin.site.register(PlanePrivilege, PlanePrivilegeAdmin)
admin.site.register(Plane, PlaneAdmin)
admin.site.register(PlaneInventory, PlaneInventoryAdmin)