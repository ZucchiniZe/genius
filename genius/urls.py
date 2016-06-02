from django.conf.urls import include, url
from django.contrib import admin

from peak.views import index

urlpatterns = [
    url(r'^$', index, name='frontpage'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^peak/', include('peak.urls', namespace='peak')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
]
