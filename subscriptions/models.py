from django.db import models
from django.core.validators import MinValueValidator
from rest_framework.exceptions import ValidationError


class Subscriptions(models.Model):
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=50, choices=)
    description = models.TextField(blank=True)
    subscriptions_type = models.CharField(max_length=255)
    updated_subscription = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0)])
    validity_period = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    training_content = models.TextField(blank=True)
    visits_limit = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    start_date = models.DateField()
    end_date = models.DateField()
    activation_date = models.DateField(null=True, blank=True)
    started_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    remaining_visits = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    def clear(self):
        if not self.title.strip():
            raise ValidationError("Имя не должно быть пустым")
        if not self.subscriptions_type.strip():
            raise ValidationError("subscriptions type не должен быть пустым")
        if self.price < 0:
            raise ValidationError("цена не может быть отрицательной")


class SubscriptionsFreeze(models.Model):
    subscriptions = models.ForeignKey(
        Subscriptions,
        on_delete=models.CASCADE,
        related_name="freezes",
    )
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)
