from django.db import models
from django.db.models import ForeignKey, ManyToManyField, OneToOneField
from django.db.models.fields import TextField, TimeField
from attendance.models import CheckIn
from users.models import Client


# Create your models here.

class WaitingList(models.Model):
    creation_time = models.TimeField()


class Booking(models.Model):
    client = models.ForeignKey(Client)
    check_in = models.OneToOneField(CheckIn)
    waiting_list = models.ManyToManyField(WaitingList)
    additional_task = models.TextField()