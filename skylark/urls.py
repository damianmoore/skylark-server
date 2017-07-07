from django.conf.urls import url
from django.contrib import admin

from notifications.views import api_register, webhook


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/register/$', api_register),
    url(r'^webhook/$', webhook),
]
