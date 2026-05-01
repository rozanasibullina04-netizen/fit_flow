from django.db import models


class VisitHistory(models.Model):
    training = models.ForeignKey(
        "schedule.Training",
        on_delete=models.CASCADE,
        related_name="visit_histories",
    )
    check_in = models.OneToOneField(
        "CheckIn",
        on_delete=models.CASCADE,
        related_name="visit_history",
        null=True,
        blank=True,
    )
    checked_in_at = models.DateTimeField()
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


class CheckIn(models.Model):
    client = models.ForeignKey(
        "users.Client",
        on_delete=models.CASCADE,
        related_name="check_ins",
    )
    checked_in_at = models.DateTimeField()
    active_subscription = models.ForeignKey(
        "subscriptions.Subscriptions",
        on_delete=models.CASCADE,
        related_name="check_ins",
    )
    time_limit = models.TimeField()
