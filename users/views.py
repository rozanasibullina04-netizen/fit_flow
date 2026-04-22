from django.shortcuts import render
from rest_framework import generics
from .models import Trainer, Admin, Client
from .serializers import TrainerSerializer, AdminSerializer, ClientSerializer
from rest_framework import viewsets


# Create your views here.

class TrainerAPiView(generics.ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class AdminAPIView(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class ClientAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer