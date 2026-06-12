from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models


name_validator = RegexValidator(
    regex=r".*[^\W\d_].*",
    message="Поле должно содержать буквы.",
)


class Trainer(models.Model):
    full_name = models.CharField(
        max_length=150,
        validators=[name_validator],
        default="Unknown trainer",
    )
    photo = models.ImageField(upload_to="trainers/", blank=True, null=True)
    specialization = models.TextField(default="General fitness")
    experience = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    rating = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    notifications = models.ManyToManyField(
        "notifications.Notifications",
        related_name="trainers",
        blank=True,
    )
    trainer_data = models.TextField(blank=True, default="")
    training = models.ForeignKey(
        "schedule.Training",
        on_delete=models.CASCADE,
        related_name="trainers",
        null=True,
        blank=True,
    )

    def clean(self):
        errors = {}
        self.full_name = self.full_name.strip()
        self.specialization = self.specialization.strip()
        self.trainer_data = self.trainer_data.strip()
        if not self.full_name:
            errors["full_name"] = "ФИО не может быть пустым."
        if not self.specialization:
            errors["specialization"] = "Специализация не может быть пустой."
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Admin(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="admin_profile",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=150, validators=[name_validator])
    trainer = models.ForeignKey(
        Trainer,
        related_name="admins",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    subscriptions = models.ForeignKey(
        "subscriptions.Subscriptions",
        on_delete=models.CASCADE,
        related_name="admins",
        null=True,
        blank=True,
    )
    booking = models.ForeignKey(
        "bookings.Booking",
        on_delete=models.CASCADE,
        related_name="admins",
        null=True,
        blank=True,
    )
    notifications = models.ForeignKey(
        "notifications.Notifications",
        on_delete=models.CASCADE,
        related_name="admins",
        null=True,
        blank=True,
    )
    check_in = models.DateTimeField(null=True, blank=True)
    training_schedule = models.TextField(blank=True, default="")
    user_list = models.TextField(blank=True, default="")

    def clean(self):
        self.name = self.name.strip()
        self.training_schedule = self.training_schedule.strip()
        self.user_list = self.user_list.strip()
        if not self.name:
            raise ValidationError({"name": "Имя не может быть пустым."})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, validators=[name_validator])
    trainer = models.ManyToManyField(
        Trainer,
        related_name="clients",
        blank=True,
    )
    admin = models.ForeignKey(
        Admin,
        related_name="clients",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    subscriptions = models.OneToOneField(
        "subscriptions.Subscriptions",
        on_delete=models.CASCADE,
        related_name="client",
        null=True,
        blank=True,
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

    def clean(self):
        self.name = self.name.strip()
        if not self.name:
            raise ValidationError({"name": "Имя не может быть пустым."})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
