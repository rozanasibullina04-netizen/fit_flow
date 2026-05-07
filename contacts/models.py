from django.db import models


class ContactList(models.Model):
    client_list = models.TextField()
    email = models.EmailField()
    phone = models.IntegerField()
    registration_date = models.DateField()