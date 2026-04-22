from django.contrib import admin
from .models import Training, TrainingType, TrainingSchedule, Gym, ScheduledEvent

# Register your models here.

admin.site.register(Training)
admin.site.register(TrainingType)
admin.site.register(TrainingSchedule)
admin.site.register(Gym)
admin.site.register(ScheduledEvent)