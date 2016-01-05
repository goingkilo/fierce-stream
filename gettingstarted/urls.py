from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import kilo.feeds.views

urlpatterns = patterns('',
    url(r'^kpaper', kilo.feeds.views.kpaper, name='kpaper'))
