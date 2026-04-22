from django.db import models
from django.db.models import DateField, TimeField, DateTimeField, ForeignKey
from django.db.models.fields import CharField, TextField, IntegerField


# Create your models here.

class Subscriptions(models.Model):
    title = models.CharField(max_length=255)
    status = models.TextField()
    subscriptions_type = models.TextField()
    price = models.IntegerField()
    validity_period = models.DateField()
    training_content = models.TextField()
    time_limit = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()
    activation_date = models.DateField()


class SubscriptionsFreeze(models.Model):
    subscriptions = models.ForeignKey(Subscriptions)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.DateTimeField()

