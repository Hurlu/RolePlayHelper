from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView),
                       url(r'^logout$', views.LogoutView),
                       url(r'^charfile', views.CharacterView),
                       )