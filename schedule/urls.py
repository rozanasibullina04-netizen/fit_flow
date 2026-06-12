from django.urls import path
from .views import (
    RoomDetailView,
    RoomListView,
    ScheduleDetailView,
    ScheduleView,
    ScheduledEventDetailView,
    ScheduledEventView,
    TrainingDetailView,
    TrainingTypeDetailView,
    TrainingTypeView,
    TrainingView,
    WorkoutDetailUpdateDeleteView,
    WorkoutListCreateView,
)

urlpatterns = [
    path('api/v1/schedule/', ScheduleView.as_view(), name='schedule'),
    path('api/v1/schedule/<int:id>/', ScheduleDetailView.as_view(), name='schedule-detail'),
    path('api/v1/workouts/', WorkoutListCreateView.as_view(), name='workout'),
    path('api/v1/workouts/<int:id>/', WorkoutDetailUpdateDeleteView.as_view(), name='workout-detail'),
    path('api/v1/rooms/', RoomListView.as_view(), name='gym'),
    path('api/v1/rooms/<int:id>/', RoomDetailView.as_view(), name='gym-detail'),
    path('api/v1/trainings/', TrainingView.as_view(), name='training'),
    path('api/v1/trainings/<int:id>/', TrainingDetailView.as_view(), name='training-detail'),
    path('api/v1/scheduled-event/', ScheduledEventView.as_view(), name='scheduled-event'),
    path('api/v1/scheduled-event/<int:id>/', ScheduledEventDetailView.as_view(), name='scheduled-event-detail'),
    path('api/v1/trainings-type/', TrainingTypeView.as_view(), name='training-type'),
    path('api/v1/trainings-type/<int:id>/', TrainingTypeDetailView.as_view(), name='training-type-detail'),
]
