from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^books$', views.books),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^newbook$', views.newbook),
    url(r'^addbook$', views.addbook),
    url(r'^user/(?P<id>\d+)$', views.user),
    url(r'^book/(?P<id>\d+)$', views.viewbook),
    url(r'^addreview/(?P<id>\d+)$', views.addreview),
    url(r'^', views.undefined)
]
