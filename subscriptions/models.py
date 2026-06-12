from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class Subscriptions(models.Model):
    STATUS_ACTIVE = "active"
    STATUS_INACTIVE = "inactive"
    STATUS_FROZEN = "frozen"
    STATUS_EXPIRED = "expired"

    STATUS_CHOICES = (
        (STATUS_ACTIVE, "Active"),
        (STATUS_INACTIVE, "Inactive"),
        (STATUS_FROZEN, "Frozen"),
        (STATUS_EXPIRED, "Expired"),
    )

    title = models.CharField(max_length=150)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_INACTIVE)
    description = models.TextField(blank=True)
    subscriptions_type = models.CharField(max_length=255)
    updated_subscription = models.DateTimeField(auto_now=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    validity_period = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    training_content = models.TextField(blank=True)
    visits_limit = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    start_date = models.DateField()
    end_date = models.DateField()
    activation_date = models.DateField(null=True, blank=True)
    started_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    remaining_visits = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    def is_active_on(self, target_date):
        if self.start_date and target_date < self.start_date:
            return False
        if self.end_date and target_date > self.end_date:
            return False
        return self.status == self.STATUS_ACTIVE and self.remaining_visits > 0

    def clean(self):
        errors = {}
        self.title = self.title.strip()
        self.subscriptions_type = self.subscriptions_type.strip()
        self.description = self.description.strip()
        self.training_content = self.training_content.strip()
        if not self.title:
            errors["title"] = "Название не может быть пустым."
        if not self.subscriptions_type:
            errors["subscriptions_type"] = "Тип подписки не может быть пустым."
        if self.end_date and self.start_date and self.end_date < self.start_date:
            errors["end_date"] = "Дата окончания не может быть раньше даты начала."
        if self.activation_date:
            if self.activation_date < self.start_date:
                errors["activation_date"] = "Дата активации не может быть раньше даты начала."
            if self.activation_date > self.end_date:
                errors["activation_date"] = "Дата активации не может быть позже даты окончания."
        if self.expires_at and self.started_at and self.expires_at <= self.started_at:
            errors["expires_at"] = "Дата окончания действия должна быть позже даты начала."
        if self.remaining_visits > self.visits_limit:
            errors["remaining_visits"] = "Количество оставшихся посещений не может превышать лимит."
        if self.status == self.STATUS_ACTIVE and self.end_date < timezone.now().date():
            errors["status"] = "Активная подписка не может быть уже просроченной."
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class SubscriptionsFreeze(models.Model):
    subscriptions = models.ForeignKey(
        Subscriptions,
        on_delete=models.CASCADE,
        related_name="freezes",
    )
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)

    def clean(self):
        errors = {}
        if self.end_date < self.start_date:
            errors["end_date"] = "Дата окончания не может быть раньше даты начала."
        if self.subscriptions_id:
            if self.start_date < self.subscriptions.start_date:
                errors["start_date"] = "Заморозка не может начаться раньше начала подписки."
            if self.end_date > self.subscriptions.end_date:
                errors["end_date"] = "Заморозка не может закончиться позже окончания подписки."
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
