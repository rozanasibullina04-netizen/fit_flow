from django.db import models
from django.db.models import TextField, ManyToManyField, OneToOneField, ForeignKey
from rest_framework.fields import TimeField, IntegerField, CharField
from users.models import Admin, Trainer, Client


# Create your models here.

class Training(models.Model):
    training_type = models.TextField()
    training_content = models.TextField()
    subscriptions_type = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    training_schedule = models.TextField()
    max_capacity = models.IntegerField()


class TrainingType(models.Model):
    title = models.CharField(max_length=255)
    duration = models.TimeField()


class TrainingSchedule(models.Model):
    training = models.ManyToManyField(Training)
    start_time = models.TimeField()
    end_time = models.TimeField()


class Gym(models.Model):
    title = models.CharField(max_length=255)
    equipment = models.TextField()
    training = models.ManyToManyField(Training)
    admin = models.ForeignKey(Admin)
    trainer = models.ManyToManyField(Trainer)
    client = models.ManyToManyField(Client)


class ScheduledEvent(models.Model):
    start_time = models.TimeField()
    duration = models.TimeField()
    training_schedule = models.ForeignKey(TrainingSchedule)