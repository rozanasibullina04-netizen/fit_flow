from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


class WaitingList(models.Model):
    training = models.ForeignKey(
        "schedule.Training",
        on_delete=models.CASCADE,
        related_name="waiting_list_entries",
    )
    client = models.ForeignKey(
        "users.Client",
        on_delete=models.CASCADE,
        related_name="waiting_list_entries",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["training", "client"],
                name="unique_waiting_list_entry",
            )
        ]

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Booking(models.Model):
    client = models.ForeignKey(
        "users.Client",
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    check_in = models.OneToOneField(
        "attendance.CheckIn",
        on_delete=models.CASCADE,
        related_name="booking",
        null=True,
        blank=True,
    )
    waiting_list = models.ManyToManyField(
        WaitingList,
        blank=True,
        related_name="bookings",
    )
    additional_task = models.TextField(blank=True)
    active_subscription = models.ForeignKey(
        "subscriptions.Subscriptions",
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    free_seats = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    def clean(self):
        errors = {}
        if self.additional_task is not None:
            self.additional_task = self.additional_task.strip()
        if getattr(self.active_subscription, "client_id", None) and self.active_subscription.client_id != self.client_id:
            errors["active_subscription"] = "Подписка должна принадлежать выбранному клиенту."
        if self.check_in_id and self.check_in.client_id != self.client_id:
            errors["check_in"] = "Отметка посещения должна принадлежать выбранному клиенту."
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
