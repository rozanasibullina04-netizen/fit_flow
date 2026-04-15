from django.db import models
from django.contrib.auth.models import User
from django.db.models import OneToOneField, ForeignKey
from django.db.models.fields import TextField
from django.template.defaultfilters import length
from rest_framework.fields import CharField, DateTimeField


# Create your models here.

class Trainer(models.Model):
    name = CharField(max_length=255)
    notifications = TextField()
    training_schedule = TextField()
    visit_history = DateTimeField()

class Client(models.Model):
    name = CharField(max_length=255)
    subscritions =
    notifications = TextField()
    training_schedule = TextField()
    trainer = ForeignKey(Trainer)
    visit_history = DateTimeField()

class Admin(models.Model):
    name = CharField(max_length=255)
    subsritions =
    booking = TextField()
    notifications = TextField()

