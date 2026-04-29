from django.urls import path
from .views import ScheduleView, WorkoutListCreateView, WorkoutDetailUpdateDeleteView, RoomListView

urlpatterns = [
    path('api/v1/schedule/', ScheduleView.as_view(), name='schedule'),
    path('api/v1/workouts/', WorkoutListCreateView.as_view(), name='workout'),
    path('api/v1/workouts/<int:id>/', WorkoutDetailUpdateDeleteView.as_view(), name='workout-detail'),
    path('api/v1/rooms/', RoomListView.as_view(), name='gym')
]