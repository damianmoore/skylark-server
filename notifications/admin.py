from django.contrib import admin

from .models import Device, Notification, Filter


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'last_active')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'webhook', 'created')


@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
