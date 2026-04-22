from django.db import models
from django.db.models.fields import TextField


# Create your models here.

class Notifications(models.Model):
    content = models.TextField()