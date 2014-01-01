# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from django.db import models
from hawaii import const
from hawaii.apps.ueditor.fields import UEditorField


class Hotel(models.Model):
    class Meta:
        db_table = u'hawaii_hotel'
        verbose_name = verbose_name_plural = u"酒店管理"

    def __unicode__(self):
        return self.name

    name = models.CharField(u"酒店名", max_length=const.DB_NORMAL_LENGTH, db_index=True)
    city = models.CharField(u"城市", max_length=const.DB_NORMAL_LENGTH)
    information = UEditorField(u"正文", default="", blank=True, null=True)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "information": self.information
        }

class HotelDay(models.Model):
    class Meta:
        db_table = u'hawaii_hotel_day'
        verbose_name = verbose_name_plural = u"天"
        ordering = ['number']

    number = models.SmallIntegerField(u"周几", default=1, unique=True)
    name = models.CharField(u"名字", max_length=const.DB_NORMAL_LENGTH, default=u"星期一", unique=True)

    def __unicode__(self):
        return self.name


class HotelInventory(models.Model):
    class Meta:
        db_table = u'hawaii_hotel_inventory'
        verbose_name = verbose_name_plural = u"价格和库存管理"

    def __unicode__(self):
        return "%s" % (self.hotel)

    hotel = models.ForeignKey(Hotel, verbose_name=u"酒店", related_name="inventories")
    amount = models.IntegerField(u"库存数量", default=0)
    inventory_type = models.CharField(u"类型", default="海景房", max_length=const.DB_NORMAL_LENGTH)

    price = models.FloatField(u"价格", default=0.0)

    days_limit = models.IntegerField(u"起订天数", default=0)
    amount_limit = models.IntegerField(u"起订间数", default=0)
    breakfast = models.BooleanField(u"是否含早", default=False)

    begin = models.DateField(u"开始时间")
    end = models.DateField(u"结束时间")
    days = models.ManyToManyField(HotelDay, verbose_name=u"周几", blank=True)
    remark = models.CharField(u"备注信息", max_length=const.DB_CONTENT_LENGTH, default="", blank=True)


class HotelPrivilege(models.Model):
    class Meta:
        db_table = u'hawaii_hotel_privilege'
        verbose_name = verbose_name_plural = u"酒店优惠"

    def __unicode__(self):
        return "%s: %s" % (self.hotel, self.title)

    hotel = models.ForeignKey(Hotel, verbose_name=u"酒店", related_name="privileges")
    title = models.CharField(u"优惠标题", max_length=const.DB_TITLE_LENGTH)
    description = models.CharField(u"优惠描述", max_length=const.DB_CONTENT_LENGTH, blank=True, default="")


class HotelProduct(models.Model):
    class Meta:
        db_table = u'hawaii_hotel_product'
        verbose_name = verbose_name_plural = u"所有酒店产品"

    def __unicode__(self):
        return "%s: %s %s" % (self.name, self.city, self.check_in_time)

    inventory = models.ForeignKey(HotelInventory, verbose_name=u"库存", editable=False, related_name="products")
    name = models.CharField(u"酒店名", max_length=const.DB_NORMAL_LENGTH)
    city = models.CharField(u"城市", max_length=const.DB_NORMAL_LENGTH)

    amount = models.IntegerField(u"库存数量", default=0)
    inventory_type = models.CharField(u"类型", default="海景房", max_length=const.DB_NORMAL_LENGTH)

    price = models.FloatField(u"价格", default=0.0)

    days_limit = models.IntegerField(u"起订天数", default=0)
    amount_limit = models.IntegerField(u"起订间数", default=0)
    breakfast = models.BooleanField(u"是否含早", default=False)
    remark = models.CharField(u"备注信息", max_length=const.DB_CONTENT_LENGTH, default="", blank=True)

    check_in_time = models.DateTimeField(u"入住时间")

    @property
    def html(self):
        return "%s" % self.name

    @classmethod
    def bulk_create_products(cls, inventory, dates):
        objects = []
        for date in dates:
            product = cls(
                inventory=inventory,
                name=inventory.hotel.name,
                city=inventory.hotel.city,

                amount=inventory.amount,
                inventory_type=inventory.inventory_type,
                price=inventory.price,
                days_limit=inventory.days_limit,
                amount_limit=inventory.amount_limit,
                breakfast=inventory.breakfast,
                remark=inventory.remark,
                check_in_time=date,
            )
            objects.append(product)
        cls.objects.bulk_create(objects)

    def to_json(self):
        return {
            "name": self.name,
            "city": self.city,
            "inventory_type": self.inventory_type,
            "price": self.price,
            "breakfast": self.breakfast,
            "remark": self.remark
        }