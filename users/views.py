from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from .models import Trainer, Admin, Client
from .serializers import TrainerSerializer, TrainerDetailSerializer, AdminSerializer, AdminUserSerializer, \
    ClientSerializer, AdminSubscriptionListSerializer, AdminSubscriptionUpdateSerializer


class TrainerListView(generics.ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class TrainerDetailView(generics.RetrieveAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerDetailSerializer


class AdminListView(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class AdminUserListView(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminUserSerializer


class AdminSubscriptionListView(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSubscriptionListSerializer


class AdminSubscriptionUpdateView(generics.UpdateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSubscriptionUpdateSerializer


class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class AdminStatsOverviewView(APIView):
    pass