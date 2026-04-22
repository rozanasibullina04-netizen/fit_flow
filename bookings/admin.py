from django.contrib import admin
from .models import WaitingList, Booking

# Register your models here.

admin.site.register(WaitingList)
admin.site.register(Booking)
