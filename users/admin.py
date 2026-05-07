from django.contrib import admin
from .models import Trainer, Admin, Client


admin.site.register(Trainer)
admin.site.register(Admin)
admin.site.register(Client)