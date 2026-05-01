from django.db import models


class TrainingType(models.Model):
    title = models.CharField(max_length=255)
    duration = models.DurationField()


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


class TrainingSchedule(models.Model):
    training = models.ForeignKey(
        Training,
        on_delete=models.CASCADE,
        related_name="schedules",
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    workout_list = models.TextField()
    training_data = models.TextField()


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


class ScheduledEvent(models.Model):
    training_schedule = models.ForeignKey(
        TrainingSchedule,
        on_delete=models.CASCADE,
        related_name="events",
    )
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.DurationField()
    trainer = models.ForeignKey(
        "users.Trainer",
        on_delete=models.CASCADE,
        related_name="scheduled_events",
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
    free_seats = models.PositiveIntegerField()
