from django.conf.urls import patterns, url
from skim import views

urlpatterns = patterns('',
    url(r'^detil/$', views.skim, name='skim'),
    url(r'^imformation', views.imfor, name='imfo'),
    url(r'^site_media/(?P<path>.*)','django.views.static.serve',
        {'document_root':'/honey/static/uplodeimages'}),
    url(r'^detil/single-page.html', views.display, name='dis'),

    # url(r'^upimg', views.up_img, name='up_img'),
    # url(r'submiit', views.submit, name='sub'),
)