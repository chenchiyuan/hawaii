# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from django.db import models
from hawaii import const


class Day(models.Model):
    class Meta:
        db_table = u'hawaii_day'
        verbose_name = verbose_name_plural = u"天"
        ordering = ['number']

    number = models.SmallIntegerField(u"周几", default=1, unique=True)
    name = models.CharField(u"名字", max_length=const.DB_NORMAL_LENGTH, default=u"星期一", unique=True)

    def __unicode__(self):
        return self.name


class Flight(models.Model):
    class Meta:
        db_table = u'hawaii_flight'
        verbose_name = verbose_name_plural = u"航班"

    def __unicode__(self):
        return "%s %s %s" % (self.number, self.type, self.company)

    number = models.CharField(u"航班号", max_length=const.DB_NORMAL_LENGTH, db_index=True)

    company = models.CharField(u"公司名", max_length=const.DB_NORMAL_LENGTH, default=u"夏威夷航空")
    type = models.CharField(u"机型", max_length=const.DB_NORMAL_LENGTH)
    starting = models.CharField(u"出发地", max_length=const.DB_PLACE_LENGTH)
    destination = models.CharField(u"目的地", max_length=const.DB_PLACE_LENGTH)

    departure = models.TimeField(u"起飞时间")
    arrival = models.TimeField(u"到达时间")

    plus = models.BooleanField(verbose_name=u"是否+1", default=False)


class FlightPrivilege(models.Model):
    class Meta:
        db_table = u'hawaii_plane_privilege'
        verbose_name = verbose_name_plural = u"机票优惠"

    def __unicode__(self):
        return "%s: %s" % (self.plane, self.title)

    flight = models.ForeignKey(Flight, verbose_name=u"飞机", related_name="privileges")
    title = models.CharField(u"优惠标题", max_length=const.DB_TITLE_LENGTH)
    description = models.CharField(u"优惠描述", max_length=const.DB_CONTENT_LENGTH, blank=True, default="")


class FlightInventory(models.Model):
    class Meta:
        db_table = u'hawaii_plane_inventory'
        verbose_name = verbose_name_plural = u"机票库存"

    def __unicode__(self):
        return "%s" % (self.flight)

    flight = models.ForeignKey(Flight, verbose_name=u"航班", related_name="inventories")
    seat = models.IntegerField(u"库存数量", default=0)
    type = models.CharField(u"类型", default="商务舱", max_length=const.DB_NORMAL_LENGTH)

    price = models.FloatField(u"成人价格", default=0.0)
    child_price = models.FloatField(u"儿童价格", default=0.0)

    amount_limit = models.IntegerField(u"起订人数", default=0)
    baggage_limit = models.CharField(u"行李限制", max_length=const.DB_NORMAL_LENGTH, default="20KG")
    limit = models.CharField(u"其他限制", max_length=const.DB_CONTENT_LENGTH, default="不能退票", blank=True)

    begin = models.DateField(u"开始时间")
    end = models.DateField(u"结束时间")
    days = models.ManyToManyField(Day, verbose_name=u"周几", blank=True, through="FlightInventoryDayShip")


class FlightInventoryDayShip(models.Model):
    class Meta:
        db_table = u'hawaii_flight_inventory_day_ship'
        verbose_name = verbose_name_plural = u"库存天"

    inventory = models.ForeignKey(FlightInventory, verbose_name=u"库存",)
    day = models.ForeignKey(Day, verbose_name=u"天", )