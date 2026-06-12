from django.urls import path
from .views import BookingDetailView, BookingListCreateView, BookingWaitAPIView, WaitingListView


urlpatterns = [
    path('api/v1/waiting-list/', WaitingListView.as_view(),
         name='waiting-list'),
    path('api/v1/booking/', BookingListCreateView.as_view(),
         name='booking'),
    path('api/v1/booking/<int:id>/', BookingDetailView.as_view(),
         name='booking-detail'),
    path('api/v1/trainings/<int:training_id>/waitlist/', BookingWaitAPIView.as_view(),
         name='booking_wait')
]
