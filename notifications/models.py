from django.db import models


class Notifications(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    notifications_list = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
