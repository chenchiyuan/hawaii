# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import requests


def send_email(from_email, to_email, subject="", html=""):
    url = "https://sendcloud.sohu.com/webapi/mail.send.xml"
    params = {
        "api_user": "postmaster@zoneke.sendcloud.org",
        "api_key": "Rdtk4b9f",
        "from": from_email,
        "to": to_email,
        "subject": subject,
        "html": html
    }
    r = requests.post(url, data=params)


def test():
    from_email = "zoneke.ccy@gmail.com"
    to_email = "chenchiyuan03@gmail.com"
    subject = "这是测试邮件"
    html = "Hello World"
    send_email(from_email, to_email, subject, html)