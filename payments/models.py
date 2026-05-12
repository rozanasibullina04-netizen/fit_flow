from django.db import models


class Payment(models.Model):
    payment_id = models.IntegerField()
    status = models.IntegerField()
    subscription = models.OneToOneField(
        "subscriptions.Subscriptions",
        related_name="payments",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    payment_list = models.TextField()
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)