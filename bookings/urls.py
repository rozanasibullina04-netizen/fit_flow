from django.urls import path
from .views import WaitingListView, BookingListCreateView, BookingWaitAPIView


urlpatterns = [
    path('api/v1/waiting-list/', WaitingListView.as_view(),
         name='waiting-list'),
    path('api/v1/booking/', BookingListCreateView.as_view(),
         name='booking'),
    path('/api/v1/booking/<int:workout_id>/waitlist/', BookingWaitAPIView.as_view(),
         name='booking_wait')
]