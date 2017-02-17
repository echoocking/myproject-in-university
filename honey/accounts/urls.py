#coding:utf-8
from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
    url(r'^login', views.index),

    url(r'^register/$', views.register, name='register'),
    url(r'^denglu/$', views.login, name='lo'),
    url(r'^orig', views.orig),
    url(r'^logout', views.logout),
    # url(r'^userimfor', views.userimfordetil),
    #url(r'^login/$', views.register, name='register'),

)
    # url(r'^/login/login', views.login),#与action 有关
    # url(r'register/', views.register),

#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^blog/register/$','blog.views.register'),
#     url(r'^blog/login/$','blog.views.login'),
#     url(r'^blog/index/$','blog.views.index'),
#     url(r'^blog/regsuc/$','blog.views.regsuc'),
#     url(r'^blog/logout/$','blog.views.logout'),
#     url(r'^blog/changepwd/$','blog.views.changePwd'),
# )
