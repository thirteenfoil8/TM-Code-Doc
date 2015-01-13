from django.conf.urls import patterns, include, url
from django.contrib import admin
from exercises.views import index, create, base, find, exercises

urlpatterns = patterns('',
    url(r'^$', index, name="index"),
    url(r'^create/$', create, name="create"),
    url(r'^base/$', base, name="base"),
    url(r'^find/$', find, name="find"),
    url(r'^exercises/(\d+)/$', exercises, name="exercises")
)