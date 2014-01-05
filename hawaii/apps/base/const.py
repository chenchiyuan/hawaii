# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from datetime import datetime

DEADLINE_MUCH = 72
DEADLINE_LESS = 24
DAYS_LIMIT = 14

def get_email_title(**kwargs):
    datetime_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    return u"新订单: %s " % datetime_str