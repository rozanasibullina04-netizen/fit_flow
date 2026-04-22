from django.contrib import admin
from .models import Subscriptions, SubscriptionsFreeze

# Register your models here.

admin.site.register(Subscriptions)
admin.site.register(SubscriptionsFreeze)
