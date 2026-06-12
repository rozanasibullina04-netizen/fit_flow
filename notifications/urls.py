from django.urls import path
from .views import NotificationDetailView, NotificationReadView, NotificationsListView


urlpatterns = [
    path('api/v1/notifications/', NotificationsListView.as_view(), name='notifications'),
    path('api/v1/notifications/<int:id>/', NotificationDetailView.as_view(), name='notifications-detail'),
    path('api/v1/notifications/<int:id>/read/', NotificationReadView.as_view(), name='notifications-read'),
]
