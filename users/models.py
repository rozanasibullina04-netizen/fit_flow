from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from rest_framework.fields import CharField, DateTimeField, IntegerField
from bookings.models import Booking
from notifications.models import Notifications
from schedule.models import Training
from subscriptions.models import Subscriptions


# Create your models here.

class Trainer(models.Model):
    full_name = models.CharField(max_length=255)
    photo = models.ImageField()
    trainer_id = models.IntegerField()
    specialization = models.TextField()
    experience = models.IntegerField()
    rating = models.IntegerField()
    # admin = models.ForeignKey(Admin, related_name='admin', on_delete=models.CASCADE)
    notifications = models.ManyToManyField(Notifications)
    trainer_data = TextField()
    training = models.ForeignKey(Training)


class Admin(models.Model):
    name = models.CharField(max_length=255)
    trainer = models.ForeignKey(Trainer, related_name='admin', on_delete=models.CASCADE)
    subscriptions = models.ForeignKey(Subscriptions)
    booking = models.ForeignKey(Booking)
    notifications = models.ForeignKey(Notifications)
    check_in = models.DateTimeField()
    training_schedule = models.TextField()
    user_list = models.TextField()


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    trainer = models.ManyToManyField(Trainer, related_name='client')
    admin = models.ForeignKey(Admin, related_name='client', on_delete=models.CASCADE)
    subscriptions = models.OneToOneField(Subscriptions)
    notifications = models.ManyToManyField(Notifications)
    training = models.ManyToManyField(Training)

