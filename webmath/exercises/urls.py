from django.conf.urls import patterns, include, url
from django.contrib import admin
from exercises.views import index, create, base, find, resolve, correction, search, done

urlpatterns = patterns('',
    url(r'^$', index, name="index"),
    url(r'^create/$', create, name="create"),
    url(r'^base/$', base, name="base"),
    url(r'^find/$', find, name="find"),
    url(r'^done/(\d+)/$', done, name="done"),
    url(r'^resolve/(\d+)/$', resolve, name="resolve"),
    url(r'^correction/(\d+)/$', correction, name='correction'),
    url(r'^search/', search, name="search"),
)