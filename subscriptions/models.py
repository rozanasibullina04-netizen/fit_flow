from django.db import models


class Subscriptions(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    subscriptions_type = models.CharField(max_length=255)
    updated_subscription = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField()
    validity_period = models.PositiveIntegerField()
    training_content = models.TextField(blank=True)
    visits_limit = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    activation_date = models.DateField(null=True, blank=True)
    started_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    remaining_visits = models.PositiveIntegerField()


class SubscriptionsFreeze(models.Model):
    subscriptions = models.ForeignKey(
        Subscriptions,
        on_delete=models.CASCADE,
        related_name="freezes",
    )
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)
