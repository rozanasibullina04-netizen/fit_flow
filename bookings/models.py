from django.core.exceptions import ValidationError
from django.db import models


class WaitingList(models.Model):
    training = models.ForeignKey(
        "schedule.Training",
        on_delete=models.CASCADE,
        related_name="waiting_list_entries",)
    client = models.ForeignKey(
        "users.Client",
        on_delete=models.CASCADE,
        related_name="waiting_list_entries",
    )
    created_at = models.DateTimeField(auto_now_add=True)


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
    free_seats = models.PositiveIntegerField()
    def clean(self):
        if not self.additional_task.strip():
            raise ValidationError("additional task должно быть заполнено")
        if not self.free_seats.strip() < 0:
            raise ValidationError("free seats не должен быть отрицательным")
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
