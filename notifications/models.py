import uuid

from django.db import models
from django.utils import timezone


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    created = models.DateTimeField()
    last_active = models.DateTimeField()
    firebase_token = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.created:
            self.created = now
        self.last_active = now
        super(Device, self).save(*args, **kwargs)


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField()
    title = models.TextField()
    body = models.TextField()
