# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('hawaii.apps.base.urls')),
    url(r'^editor/', include('hawaii.apps.ueditor.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^plane/', include('hawaii.apps.plane.urls')),
    url(r'^weixin/', include('hawaii.apps.weixin.urls')),
    url(r'^hotels/', include('hawaii.apps.hotel.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    #(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT, 'show_indexes': True}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)