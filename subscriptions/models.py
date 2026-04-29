from django.db import models
from django.db.models import DateField, TimeField, DateTimeField, ForeignKey
from django.db.models.fields import CharField, TextField, IntegerField


# Create your models here.

class Subscriptions(models.Model):
    title = models.CharField(max_length=255)
    status = models.TextField()
    description = TextField()
    subscriptions_type = models.TextField()
    updated_subscription = models.DateTimeField()
    price = models.IntegerField()
    validity_period = models.DateField()
    training_content = models.TextField()
    visits_limit = models.DateTimeField()
    start_date = models.DateField()
    end_date = models.DateField()
    activation_date = models.DateField()
    started_at = models.TimeField()
    expires_at = models.TimeField()
    remaining_visits = models.IntegerField()


class SubscriptionsFreeze(models.Model):
    subscriptions = models.ForeignKey(Subscriptions,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.DateTimeField()

