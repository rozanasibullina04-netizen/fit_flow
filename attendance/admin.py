from django.contrib import admin
from .models import VisitHistory, CheckIn

# Register your models here.

admin.site.register(VisitHistory)
admin.site.register(CheckIn)