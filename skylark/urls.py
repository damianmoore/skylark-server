from django.conf.urls import url
from django.contrib import admin

from notifications.views import api_register, api_notification, webhook


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/register/$', api_register),
    url(r'^api/notification/$', api_notification),
    url(r'^webhook/(?P<name>[\w-]+)/$', webhook),
    url(r'^webhook/$', webhook),
]
