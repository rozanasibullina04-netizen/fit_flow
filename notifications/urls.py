from django.urls import path
from .views import NotificationsListView


urlpatterns = [
    path('api/v1/notifications/', NotificationsListView.as_view(), name='notifications')
]