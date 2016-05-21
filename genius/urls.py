from django.conf.urls import include, url
from django.contrib import admin

from til.views import index

urlpatterns = [
    url(r'^$', index, name='frontpage'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^til/', include('til.urls', namespace='til')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hijack/', include('hijack.urls')),
]
