# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function


class Flight(object):
    def __init__(self, number, from_city, to_city, company, departure, arrival, amount):
        self.number = number
        self.from_city = from_city
        self.to_city = to_city
        self.company = company
