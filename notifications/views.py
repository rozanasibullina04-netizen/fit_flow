from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Notifications
from .serializers import NotificationsListSerializer


class NotificationsListView(generics.ListAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsListSerializer


class NotificationReadView(APIView):
    pass