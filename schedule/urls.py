from django.urls import path
from .views import ScheduleView, WorkoutListCreateView, WorkoutDetailUpdateDeleteView, RoomListView, \
    TrainingView, ScheduledEventView, TrainingTypeView

urlpatterns = [
    path("/api/v1/schedule/", ScheduleView.as_view(), name="schedule"),
    path("/api/v1/workouts/", WorkoutListCreateView.as_view(), name="workout"),
    path("/api/v1/workouts/<int:id>/", WorkoutDetailUpdateDeleteView.as_view(), name="workout-detail"),
    path("/api/v1/rooms/", RoomListView.as_view(), name="gym"),
    path("/api/v1/trainings/", TrainingView.as_view(), name="training"),
    path("/api/v1/scheduled-event/", ScheduledEventView.as_view(), name="scheduled-event"),
    path("/api/v1/trainings-type/", TrainingTypeView.as_view(), name="training-type")
]