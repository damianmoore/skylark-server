import uuid

from django.db import models
from django.utils import timezone


DEVICE_TYPE_CHOICES = (
    ('FI', 'Firebase'),
    ('WP', 'Web Push'),
)


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=2, choices=DEVICE_TYPE_CHOICES)
    enabled = models.BooleanField(default=False)
    created = models.DateTimeField()
    last_active = models.DateTimeField()
    firebase_token = models.TextField(blank=True, null=True)
    web_push_endpoint = models.TextField(blank=True, null=True)
    web_push_p256dh = models.TextField(blank=True, null=True)
    web_push_auth = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.created:
            self.created = now
        self.last_active = now
        super(Device, self).save(*args, **kwargs)


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField()
    title = models.TextField(blank=True)
    body = models.TextField(blank=True)
    icon = models.TextField(blank=True)
    color = models.TextField(blank=True)
    webhook = models.CharField(max_length=30, blank=True)
    raw_data = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.created:
            self.created = now
        super(Notification, self).save(*args, **kwargs)


class Filter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, blank=True)
    title = models.TextField(blank=True)
    body = models.TextField(blank=True)
    icon = models.TextField(blank=True)
    color = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
