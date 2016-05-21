from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^tag/(?P<tag>.*)/$', views.index_tag, name='index_tag'),
    url(r'^user/(?P<username>.*)/$', views.index_user, name='index_user'),
    url(r'^private/$', views.personal_index, name='private'),
]
