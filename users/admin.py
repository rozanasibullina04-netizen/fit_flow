from django.contrib import admin
from .models import Trainer, Admin, Client

# Register your models here.

admin.site.register(Trainer)
admin.site.register(Admin)
admin.site.register(Client)