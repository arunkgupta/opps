#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from django.conf.urls import patterns, url

from .views import OppsDetail, OppsList, Search


urlpatterns = patterns(
    '',
    url(r'^$', OppsList.as_view(), name='home'),
    url(r'^search/', Search(), name='search'),
    url(r'^(?P<channel__long_slug>[\w//-]+)/(?P<slug>[\w-]+)$',
        OppsDetail.as_view(), name='open'),
    url(r'^(?P<channel__long_slug>[\w\b//-]+)/$', OppsList.as_view(),
        name='channel'),
)
