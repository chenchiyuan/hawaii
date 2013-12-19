# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from django.db import models
from hawaii import const


class Plane(models.Model):
    class Meta:
        db_table = u'hawaii_plane'
        verbose_name = verbose_name_plural = u"机票"

    def __unicode__(self):
        return "%s %s %s" % (self.number, self.type, self.company)

    number = models.CharField(u"航班号", max_length=const.DB_NORMAL_LENGTH, primary_key=True)

    company = models.CharField(u"公司名", max_length=const.DB_NORMAL_LENGTH, default=u"夏威夷航空")
    type = models.CharField(u"机型", max_length=const.DB_NORMAL_LENGTH)


class PlanePrivilege(models.Model):
    class Meta:
        db_table = u'hawaii_plane_privilege'
        verbose_name = verbose_name_plural = u"机票优惠"

    def __unicode__(self):
        return "%s: %s" %(self.plane, self.title)

    plane = models.ForeignKey(Plane, verbose_name=u"飞机", related_name="privileges")
    title = models.CharField(u"优惠标题", max_length=const.DB_TITLE_LENGTH)
    description = models.CharField(u"优惠描述", max_length=const.DB_CONTENT_LENGTH, blank=True, default="")


class PlaneInventory(models.Model):
    class Meta:
        db_table = u'hawaii_plane_inventory'
        verbose_name = verbose_name_plural = u"机票库存"

    def __unicode__(self):
        return "%s %s" %(self.plane, self.arrival)

    plane = models.ForeignKey(Plane, verbose_name=u"飞机", related_name="inventories")
    starting = models.CharField(u"出发地", max_length=const.DB_PLACE_LENGTH)
    destination = models.CharField(u"目的地", max_length=const.DB_PLACE_LENGTH)

    departure = models.DateTimeField(u"起飞时间")
    arrival = models.DateTimeField(u"到达时间")
    seat = models.IntegerField(u"库存数量", default=0)
    type = models.CharField(u"类型", default="商务舱", max_length=const.DB_NORMAL_LENGTH)

    price = models.FloatField(u"成人价格", default=0.0)
    child_price = models.FloatField(u"儿童价格", default=0.0)

    amount_limit = models.IntegerField(u"起订人数", default=0)
    baggage_limit = models.CharField(u"行李限制", max_length=const.DB_NORMAL_LENGTH, default="20KG")
    limit = models.CharField(u"其他限制", max_length=const.DB_CONTENT_LENGTH, default="不能退票", blank=True)

    @property
    def format_departure(self):
        return self.departure.strftime(const.TIME_FORMAT)

    @property
    def format_arrival(self):
        return self.arrival.strftime(const.TIME_FORMAT)