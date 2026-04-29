from django.db import models
from django.db.models import ManyToManyField
from rest_framework.fields import DateTimeField, TimeField, UUIDField
from subscriptions.models import Subscriptions
from schedule.models import Training, Gym
from users.models import Trainer, Admin, Client


# Create your models here.

class VisitHistory(models.Model):
    training = models.ManyToManyField(Training)
    date_and_time = models.DateTimeField()
    training_id = models.IntegerField()
    check_in_time = models.DateTimeField()
    trainer = models.ManyToManyField(Trainer)
    subscriptions = models.ManyToManyField(Subscriptions)
    admin = models.ForeignKey(Admin)
    client = models.ManyToManyField(Client)
    gym = models.ManyToManyField(Gym)

class CheckIn(models.Model):
#    subscription_checks =
    visit_history = models.ManyToManyField(VisitHistory)
    client_id = models.IntegerField()
    timestamp = models.TimeField()
    active_subscription = models.DateTimeField()
#    registration_for_training =
    time_limit = models.TimeField()