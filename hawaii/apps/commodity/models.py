# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from django.db import models
from hawaii import const
from hawaii.apps.ueditor.fields import UEditorField
from hawaii.apps.weixin.libs.formatters import BasicFormatter


class Commodity(models.Model):
    class Meta:
        db_table = u'commodity'
        verbose_name = verbose_name_plural = u"目的地商品管理"

    def __unicode__(self):
        return self.name

    name = models.CharField(u"商品名", max_length=const.DB_NORMAL_LENGTH, db_index=True)
    city = models.CharField(u"城市", max_length=const.DB_NORMAL_LENGTH)
    information = UEditorField(u"正文", default="", blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None):
        if self.information:
            try:
                self.information = BasicFormatter.format(self.information)
            except:
                pass
        super(Commodity, self).save(force_insert, force_update, using)


class CommodityDay(models.Model):
    class Meta:
        db_table = u'commodity_day'
        verbose_name = verbose_name_plural = u"天"
        ordering = ['number']

    number = models.SmallIntegerField(u"周几", default=1, unique=True)
    name = models.CharField(u"名字", max_length=const.DB_NORMAL_LENGTH, default=u"星期一", unique=True)

    def __unicode__(self):
        return self.name


class CommodityInventory(models.Model):
    class Meta:
        db_table = u'commodity_inventory'
        verbose_name = verbose_name_plural = u"价格和库存管理"

    def __unicode__(self):
        return "%s" % self.commodity

    commodity = models.ForeignKey(Commodity, verbose_name=u"商品", related_name="inventories")
    amount = models.IntegerField(u"库存数量", default=0)
    inventory_type = models.CharField(u"类型", default="上午出发", max_length=const.DB_NORMAL_LENGTH)

    price = models.FloatField(u"价格", default=0.0)
    child_price = models.FloatField(u"儿童价格", default=0.0)

    amount_limit = models.IntegerField(u"起订人数", default=0)

    begin = models.DateField(u"开始时间")
    end = models.DateField(u"结束时间")
    days = models.ManyToManyField(CommodityDay, verbose_name=u"周几", blank=True)
    remark = models.CharField(u"备注信息", max_length=const.DB_CONTENT_LENGTH, default="", blank=True)


class CommodityPrivilege(models.Model):
    class Meta:
        db_table = u'commodity_privilege'
        verbose_name = verbose_name_plural = u"商品优惠"

    def __unicode__(self):
        return "%s: %s" % (self.commodity, self.title)

    commodity = models.ForeignKey(Commodity, verbose_name=u"商品", related_name="privileges")
    title = models.CharField(u"优惠标题", max_length=const.DB_TITLE_LENGTH)
    description = models.CharField(u"优惠描述", max_length=const.DB_CONTENT_LENGTH, blank=True, default="")


class CommodityProduct(models.Model):
    class Meta:
        db_table = u'commodity_product'
        verbose_name = verbose_name_plural = u"所有目的地商品"

    def __unicode__(self):
        return "%s: %s %s" % (self.name, self.city, self.check_in_time)

    inventory = models.ForeignKey(CommodityInventory, verbose_name=u"库存", editable=False, related_name="products")
    name = models.CharField(u"商品名", max_length=const.DB_NORMAL_LENGTH)
    city = models.CharField(u"城市", max_length=const.DB_NORMAL_LENGTH)

    amount = models.IntegerField(u"库存数量", default=0)
    inventory_type = models.CharField(u"类型", default="海景房", max_length=const.DB_NORMAL_LENGTH)

    price = models.FloatField(u"价格", default=0.0)
    child_price = models.FloatField(u"儿童价格", default=0.0)

    amount_limit = models.IntegerField(u"起订人数", default=0)
    remark = models.CharField(u"备注信息", max_length=const.DB_CONTENT_LENGTH, default="", blank=True)

    datetime = models.DateTimeField(u"入住时间")

    @property
    def html(self):
        return "%s" % self.name

    @classmethod
    def bulk_create_products(cls, inventory, dates):
        objects = []
        for date in dates:
            product = cls(
                inventory=inventory,
                name=inventory.commodity.name,
                city=inventory.commodity.city,

                amount=inventory.amount,
                inventory_type=inventory.inventory_type,
                price=inventory.price,
                child_price=inventory.child_price,
                amount_limit=inventory.amount_limit,
                remark=inventory.remark,
                datetime=date,
            )
            objects.append(product)
        cls.objects.bulk_create(objects)

    def to_json(self):
        return {
            "name": self.name,
            "city": self.city,
            "inventory_type": self.inventory_type,
            "price": self.price,
            "child_price": self.child_price,
            "remark": self.remark,
            "html": self.inventory.commodity.information
        }