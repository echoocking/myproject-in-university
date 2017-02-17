from django.conf.urls import patterns, url
from firpage import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^templates/login$', views.register, name='register')
       # url(r'^$', views.about, name='about'),
        #url(r'^about/$', )

)