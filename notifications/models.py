from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Notifications(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    notifications_list = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def clean(self):
        errors = {}
        self.title = self.title.strip()
        self.message = self.message.strip()
        if not self.title:
            errors["title"] = "Заголовок не может быть пустым."
        if not self.message:
            errors["message"] = "Сообщение не может быть пустым."
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
