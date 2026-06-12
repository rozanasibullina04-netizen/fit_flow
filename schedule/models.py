from datetime import timedelta

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class TrainingType(models.Model):
    title = models.CharField(max_length=255, unique=True)
    duration = models.DurationField(validators=[MinValueValidator(timedelta(minutes=1))])

    def clean(self):
        self.title = self.title.strip()
        if not self.title:
            raise ValidationError({"title": "Название не может быть пустым."})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Training(models.Model):
    training_type = models.ForeignKey(
        TrainingType,
        on_delete=models.CASCADE,
        related_name="trainings",
    )
    training_content = models.TextField()
    subscriptions_type = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    training_schedule = models.TextField(blank=True)
    max_capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def clean(self):
        errors = {}
        self.training_content = self.training_content.strip()
        self.subscriptions_type = self.subscriptions_type.strip()
        self.training_schedule = self.training_schedule.strip()
        if not self.training_content:
            errors["training_content"] = "Описание тренировки не может быть пустым."
        if not self.subscriptions_type:
            errors["subscriptions_type"] = "Тип подписки не может быть пустым."
        if self.start_time and self.end_time and self.end_time <= self.start_time:
            errors["end_time"] = "Время окончания должно быть позже времени начала."
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


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
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    description = models.TextField(blank=True)

    def clean(self):
        errors = {}
        self.title = self.title.strip()
        self.equipment = self.equipment.strip()
        self.description = self.description.strip()
        if not self.title:
            errors["title"] = "Название не может быть пустым."
        if not self.equipment:
            errors["equipment"] = "Оборудование не может быть пустым."
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


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
        Gym,
        related_name="schedules",
        blank=True,
    )
    workout_list = models.TextField()
    free_seats = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    def clean(self):
        errors = {}
        self.training_data = self.training_data.strip()
        self.workout_list = self.workout_list.strip()
        if not self.training_data:
            errors["training_data"] = "Данные тренировки не могут быть пустыми."
        if not self.workout_list:
            errors["workout_list"] = "Список упражнений не может быть пустым."
        if self.start_time and self.end_time and self.end_time <= self.start_time:
            errors["end_time"] = "Время окончания должно быть позже времени начала."
        if self.training_id and self.free_seats > self.training.max_capacity:
            errors["free_seats"] = "Количество свободных мест не может превышать вместимость тренировки."
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class ScheduledEvent(models.Model):
    training_schedule = models.ForeignKey(
        TrainingSchedule,
        on_delete=models.CASCADE,
        related_name="events",
    )
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.DurationField(validators=[MinValueValidator(timedelta(minutes=1))])
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
    free_seats = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000),
        ]
    )

    def clean(self):
        errors = {}
        if self.training_schedule_id and self.training_schedule.training_id != self.training_id:
            errors["training"] = "Выбранная тренировка должна соответствовать расписанию тренировки."
        if self.gym_id and self.free_seats > self.gym.capacity:
            errors["free_seats"] = "Количество свободных мест не может превышать вместимость зала."
        if self.training_id and self.free_seats > self.training.max_capacity:
            errors["free_seats"] = "Количество свободных мест не может превышать вместимость тренировки."
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
