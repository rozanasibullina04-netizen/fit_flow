from django.core.exceptions import ValidationError
from django.db import models


class Notifications(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    notifications_list = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def clean(self):
        if not self.title.strip():
            raise ValidationError("Название не должно быть пустым")
        if not self.message.strip():
            raise ValidationError("Поле massage не должно быть пустым")
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
