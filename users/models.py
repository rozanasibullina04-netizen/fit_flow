from django.contrib.auth.models import User
from django.db import models


class Trainer(models.Model):
    full_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="trainers/", blank=True, null=True)
    specialization = models.TextField()
    experience = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(default=0)
    notifications = models.ManyToManyField(
        "notifications.Notifications",
        related_name="trainers",
        blank=True,
    )
    trainer_data = models.TextField(blank=True)
    training = models.ForeignKey(
        "schedule.Training",
        on_delete=models.CASCADE,
        related_name="trainers",
    )


class Admin(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="admin_profile",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=255)
    trainer = models.ForeignKey(
        Trainer,
        related_name="admins",
        on_delete=models.CASCADE,
    )
    subscriptions = models.ForeignKey(
        "subscriptions.Subscriptions",
        on_delete=models.CASCADE,
        related_name="admins",
    )
    booking = models.ForeignKey(
        "bookings.Booking",
        on_delete=models.CASCADE,
        related_name="admins",
    )
    notifications = models.ForeignKey(
        "notifications.Notifications",
        on_delete=models.CASCADE,
        related_name="admins",
    )
    check_in = models.DateTimeField(null=True, blank=True)
    training_schedule = models.TextField(blank=True)
    user_list = models.TextField(blank=True)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    trainer = models.ManyToManyField(
        Trainer,
        related_name="clients",
        blank=True,
    )
    admin = models.ForeignKey(
        Admin,
        related_name="clients",
        on_delete=models.CASCADE,
    )
    subscriptions = models.OneToOneField(
        "subscriptions.Subscriptions",
        on_delete=models.CASCADE,
        related_name="client",
    )
    notifications = models.ManyToManyField(
        "notifications.Notifications",
        related_name="clients",
        blank=True,
    )
    training = models.ManyToManyField(
        "schedule.Training",
        related_name="clients",
        blank=True,
    )
