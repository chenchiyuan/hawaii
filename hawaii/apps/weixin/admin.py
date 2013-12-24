# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.contrib import admin
from models import App, Rule, MenuItem, SubscribeItem, Photo, RichText


class MenuInline(admin.TabularInline):
    model = MenuItem

    raw_id_fields = ["rule"]


class SubscribeInline(admin.TabularInline):
    model = SubscribeItem
    raw_id_fields = ["rule"]

    max_num = 1


class PhotoAdmin(admin.ModelAdmin):
    pass


class RichTextAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/static/css/admin-override.css", ),
        }

class RuleAdmin(admin.ModelAdmin):
    pass


class AppAdmin(admin.ModelAdmin):
    inlines = [
        SubscribeInline,
        MenuInline
    ]
    readonly_fields = ['app_url', 'app_token']


admin.site.register(App, AppAdmin)
admin.site.register(Rule, RuleAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(RichText, RichTextAdmin)