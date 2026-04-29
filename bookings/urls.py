from django.urls import path, include
from .views import BookingListCreateView, BookingWaitAPIView

urlpatterns = [
    path('api/v1/booking/', BookingListCreateView.as_view(),
         name='booking'),
    path('/api/v1/booking/<int:workout_id>/waitlist/', BookingWaitAPIView.as_view(),
         name='booking_wait')
]