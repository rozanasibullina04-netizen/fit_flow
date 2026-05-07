from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from .models import Subscriptions, SubscriptionsFreeze
from .serializers import SubscriptionsSerializer, SubscriptionsFreezeSerializer, SubscriptionsTypeSerializer, SubscriptionsTypeDetailSerializer, SubscriptionsDetailSerializer


# Create your views here.

class SubscriptionsListView(generics.ListAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer


class SubscriptionsDetailView(generics.RetrieveAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsDetailSerializer


class SubscriptionsTypeListView(generics.ListAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsTypeSerializer


class SubscriptionsTypeDetailView(generics.RetrieveAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsTypeDetailSerializer


class SubscriptionFreezeView(APIView):
    pass


class SubscriptionUnfreezeView(APIView):
    pass
