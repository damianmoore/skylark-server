from django.contrib import admin
from django.utils.html import format_html

from .models import Device, Notification, Filter


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'last_active')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'webhook', 'created')
    list_filter = ('webhook', 'created')
    search_fields = ('title', 'webhook')


@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_preview', 'title')

    def icon_preview(self, obj):
        return format_html('<img src="{}" style="height: 50px" />', obj.icon)
    icon_preview.short_description = 'Icon'
