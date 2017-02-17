"""honey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^firpage$', include('firpage.urls')),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{ 'document_root':settings.STATIC_PATH}),
    url(r'^accounts/', include('accounts.urls')),#email register
    url(r'^register/', include('firpage.urls'), name='register'),
    url(r'^skim/', include('skim.urls')),
    url(r'^negotiator/$', 'detil.views.show_info'),
    url(r'^search/$', 'detil.views.search'),
    url(r'^buy/$', 'buy.views.get_buy'),
    url(r'^accounts/showuserimfor', 'accounts.views.showimfor'),
    url(r'^accounts/userimfor', "accounts.views.userimfordetil")
    # url(r'^userdetil','accounts.views.userditil'),
    #url(r'^view/', include('accounts.urls')),

)
