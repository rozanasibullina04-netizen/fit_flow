from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


class Payment(models.Model):
    STATUS_PENDING = "pending"
    STATUS_PAID = "paid"
    STATUS_FAILED = "failed"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_PAID, "Paid"),
        (STATUS_FAILED, "Failed"),
    )

    payment_id = models.PositiveIntegerField(unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    subscription = models.ForeignKey(
        "subscriptions.Subscriptions",
        related_name="payments",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
    )
    payment_list = models.TextField(blank=True)

    def clean(self):
        self.payment_list = self.payment_list.strip()
        if self.subscription_id and self.amount <= 0:
            raise ValidationError({"amount": "Сумма оплаты для подписки должна быть больше нуля."})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
