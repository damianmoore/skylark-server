from django.conf.urls import url
from django.contrib import admin

from notifications.views import register_webpush, api_register_webpush, api_register_firebase, api_notification, webhook


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/webpush/$', register_webpush),
    # url(r'^service-worker.js$', ),
    url(r'^api/register/webpush/$', api_register_webpush),
    url(r'^api/register/firebase/$', api_register_firebase),
    url(r'^api/notification/$', api_notification),
    url(r'^webhook/(?P<name>[\w-]+)/$', webhook),
    url(r'^webhook/$', webhook),
]
