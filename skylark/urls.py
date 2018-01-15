from django.conf.urls import url
from django.contrib import admin

from notifications.views import api_register, api_notification, api_notifications, webhook


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/register/$', api_register),
    url(r'^api/notification/(?P<id>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})/$', api_notification),
    url(r'^api/notifications/', api_notifications),
    url(r'^webhook/(?P<name>[\w-]+)/$', webhook),
    url(r'^webhook/$', webhook),
]
