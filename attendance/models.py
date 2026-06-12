from django.core.exceptions import ValidationError
from django.db import models, transaction
from django.utils import timezone


class CheckIn(models.Model):
    client = models.ForeignKey(
        "users.Client",
        on_delete=models.CASCADE,
        related_name="check_ins",
    )
    checked_in_at = models.DateTimeField(default=timezone.now)
    active_subscription = models.ForeignKey(
        "subscriptions.Subscriptions",
        on_delete=models.CASCADE,
        related_name="check_ins",
    )
    time_limit = models.TimeField()

    def clean(self):
        errors = {}
        subscription_client_id = getattr(self.active_subscription, "client_id", None)
        if subscription_client_id and subscription_client_id != self.client_id:
            errors["active_subscription"] = "Подписка должна принадлежать выбранному клиенту."
        if self.active_subscription_id and not self.active_subscription.is_active_on(self.checked_in_at.date()):
            errors["active_subscription"] = "Подписка должна быть активна на дату посещения."
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        self.full_clean()
        with transaction.atomic():
            if is_new:
                subscription = (
                    self.active_subscription.__class__.objects.select_for_update()
                    .get(pk=self.active_subscription_id)
                )
                if not subscription.is_active_on(self.checked_in_at.date()):
                    raise ValidationError(
                        {"active_subscription": "Subscription is not available for check-in."}
                    )
                subscription.remaining_visits -= 1
                subscription.save(update_fields=["remaining_visits", "updated_subscription"])
            return super().save(*args, **kwargs)


class VisitHistory(models.Model):
    training = models.ForeignKey(
        "schedule.Training",
        on_delete=models.CASCADE,
        related_name="visit_histories",
    )
    check_in = models.OneToOneField(
        CheckIn,
        on_delete=models.CASCADE,
        related_name="visit_history",
        null=True,
        blank=True,
    )
    checked_in_at = models.DateTimeField(default=timezone.now)
    trainer = models.ForeignKey(
        "users.Trainer",
        on_delete=models.CASCADE,
        related_name="visit_histories",
    )
    subscription = models.ForeignKey(
        "subscriptions.Subscriptions",
        on_delete=models.CASCADE,
        related_name="visit_histories",
    )
    admin = models.ForeignKey(
        "users.Admin",
        on_delete=models.CASCADE,
        related_name="visit_histories",
    )
    client = models.ForeignKey(
        "users.Client",
        on_delete=models.CASCADE,
        related_name="visit_histories",
    )
    gym = models.ForeignKey(
        "schedule.Gym",
        on_delete=models.CASCADE,
        related_name="visit_histories",
    )

    def clean(self):
        errors = {}
        subscription_client_id = getattr(self.subscription, "client_id", None)
        if subscription_client_id and subscription_client_id != self.client_id:
            errors["subscription"] = "Подписка должна принадлежать выбранному клиенту."
        if self.check_in_id:
            if self.check_in.client_id != self.client_id:
                errors["check_in"] = "Отметка посещения должна принадлежать выбранному клиенту."
            if self.check_in.active_subscription_id != self.subscription_id:
                errors["check_in"] = "Подписка в отметке посещения должна совпадать с подпиской в истории посещений."
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
