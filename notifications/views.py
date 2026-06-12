from rest_framework import generics
from .models import Notifications
from .serializers import NotificationsListSerializer


class NotificationsListView(generics.ListCreateAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsListSerializer


class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsListSerializer
    lookup_field = "id"


class NotificationReadView(generics.UpdateAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsListSerializer
    lookup_field = "id"

    def perform_update(self, serializer):
        serializer.save(is_read=True)
