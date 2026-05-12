from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.exceptions import ValidationError


class TrainingType(models.Model):
    title = models.CharField(max_length=255)
    duration = models.DurationField()
    def clean(self):
        if not self.title.strip():
           raise ValidationError( "Название не должно быть пустым")
        if self.duration.strip() < 0:
            raise ValidationError("duration не должен быть отрицательным")
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Training(models.Model):
    training_type = models.ForeignKey(
        TrainingType,
        on_delete=models.CASCADE,
        related_name="trainings",
    )
    training_content = models.TextField()
    subscriptions_type = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    training_schedule = models.TextField()
    max_capacity = models.PositiveIntegerField()
    def clean(self):
        if not self.training_content.strip():
           raise ValidationError( "training content не должен быть пустым")
        if not self.subscriptions_type.strip():
           raise ValidationError( "subscriptions type не должно быть пустым")
        if not self.max_capacity.strip() < 0:
            raise ValidationError("max capacity не должен быть отрицательным")
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class TrainingSchedule(models.Model):
    trainer = models.ManyToManyField(
        "users.Trainer",
        related_name="schedules",
        blank=True,
    )
    training = models.ForeignKey(
        Training,
        on_delete=models.CASCADE,
        related_name="schedules",
    )
    training_data = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    gym = models.ManyToManyField(
        "schedule.Gym",
        related_name="schedules",
        blank=True,
    )
    workout_list = models.TextField()
    free_seats = models.PositiveIntegerField()
    def clean(self):
        if self.training_data.strip():
            raise ValidationError("training data не должен быть пустым")
        if self.workout_list.strip():
            raise ValidationError("workout list не должен быть пустым")
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Gym(models.Model):
    title = models.CharField(max_length=255)
    equipment = models.TextField()
    trainings = models.ManyToManyField(Training, related_name="gyms", blank=True)
    admin = models.ForeignKey(
        "users.Admin",
        on_delete=models.CASCADE,
        related_name="gyms",
    )
    trainers = models.ManyToManyField(
        "users.Trainer",
        related_name="gyms",
        blank=True,
    )
    clients = models.ManyToManyField(
        "users.Client",
        related_name="gyms",
        blank=True,
    )
    capacity = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    def clean(self):
        if not self.title.strip():
           raise ValidationError( "Название не должно быть пустым")
        if not self.equipment.strip():
           raise ValidationError( "equipment не должно быть пустым")
        if not self.capacity.strip() < 0:
            raise ValidationError("capacity не должен быть отрицательным")
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class ScheduledEvent(models.Model):
    training_schedule = models.ForeignKey(
        TrainingSchedule,
        on_delete=models.CASCADE,
        related_name="events",
    )
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.DurationField()
    trainer = models.ManyToManyField(
        "users.Trainer",
        related_name="scheduled_events",
        blank=True,
    )
    training = models.ForeignKey(
        Training,
        on_delete=models.CASCADE,
        related_name="scheduled_events",
    )
    gym = models.ForeignKey(
        Gym,
        on_delete=models.CASCADE,
        related_name="scheduled_events",
    )
    free_seats = models.PositiveIntegerField(validators=[
        MinValueValidator(1, message="Минимальное колличество мест 1"),
        MaxValueValidator(20, message="Максимальное колличество мест 20")
    ])
    def clean(self):
        if self.duration.strip() < 0:
            raise ValidationError("duration не должен быть отрицательным")
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
