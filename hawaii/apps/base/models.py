# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db import models


class City(models.Model):
    class Meta:
        db_table = u'city'
        verbose_name = verbose_name_plural = u"城市管理"
        ordering = ['-priority']

    def __unicode__(self):
        return "%s: %s" % (self.name, self.code)

    code = models.CharField(u"城市三字码", max_length=16, unique=True, help_text=u"城市的三字码，用于航班搜索。")
    name = models.CharField(u"城市名", max_length=32, help_text="城市的显示名称")
    show_from = models.BooleanField(u"出发城市显示", default=False, help_text=u"勾选之后, 用户可在出发城市中选择该城市。")
    show_to = models.BooleanField(u"抵达城市显示", default=False, help_text=u"勾选之后，用户可在抵达城市中选择该城市。")
    priority = models.IntegerField(u"优先级", default=0, help_text=u"数字越大，越优先显示")

    @classmethod
    def get_name_by_code(cls, code):
        try:
            city = City.objects.get(code=code)
            return city.name
        except cls.DoesNotExist:
            return code


class Company(models.Model):
    class Meta:
        db_table = u'company'
        verbose_name = verbose_name_plural = u"航空公司管理"

    def __unicode__(self):
        return "%s: %s" % (self.name, self.code)

    code = models.CharField(u"航空公司编码", max_length=16, unique=True, help_text=u"航空公司编码，用于航班搜索。")
    name = models.CharField(u"公司名", max_length=32, help_text="公司的显示名称")

    @classmethod
    def get_name_by_code(cls, code):
        try:
            company = cls.objects.get(code=code)
            return company.name
        except cls.DoesNotExist:
            return code