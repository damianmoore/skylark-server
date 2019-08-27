import uuid

from django.db import models
from django.utils import timezone


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    created = models.DateTimeField()
    last_active = models.DateTimeField()
    firebase_token = models.CharField(max_length=200)
    approved = models.BooleanField(default=False)

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
    webhook = models.CharField(max_length=30, blank=True, null=True)
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
