from django.db import models
from django.db.models.fields import TextField


# Create your models here.

class Notifications(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    notifications_list = models.TextField()
    is_read = models.TextField()
    created_at = models.DateTimeField()