from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.edit, name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit$', views.edit, name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.delete, name='delete'),
]