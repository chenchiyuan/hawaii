# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):
    title = u"夏威夷航空管理系统"

    def init_with_context(self, context):
        site_name = u"夏威夷"

        self.children.append(modules.ModelList(
            u"微信管理",
            column=1,
            collapsible=True,
            models=(
                'hawaii.apps.weixin.models.apps.App',
                'hawaii.apps.weixin.models.rules.Rule',
                'hawaii.apps.weixin.models.photos.Photo',
                'hawaii.apps.weixin.models.photos.RichText'
            )
        ))

        self.children.append(modules.ModelList(
            u"机票管理",
            column=1,
            collapsible=True,
            models=(
                'hawaii.apps.plane.models.Flight',
                'hawaii.apps.plane.models.FlightInventory',
                'hawaii.apps.plane.models.FlightProduct',
            ),
        ))

        self.children.append(modules.ModelList(
            u"酒店管理",
            column=1,
            collapsible=True,
            models=(
                'hawaii.apps.hotel.models.Hotel',
                'hawaii.apps.hotel.models.HotelInventory',
                'hawaii.apps.hotel.models.HotelProduct',
            ),
        ))