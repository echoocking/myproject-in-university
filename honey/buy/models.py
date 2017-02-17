from django.conf.urls import patterns, url
from django.db import models

from buy import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  # url(r'^negotiator/$', views.show_info),
  # url(r'^search$', views.serach),
  # url(r'^bookname/$', 'blog.views.show_bookname'),
    # url(r'^upimg', views.up_img, name='up_img'),
    # url(r'submiit', views.submit, name='sub'),
)