from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Subscriptions, SubscriptionsFreeze
from .serializers import SubscriptionsSerializer, SubscriptionsFreezeSerializer, SubscriptionsTypeSerializer, SubscriptionsTypeDetailSerializer, SubscriptionsDetailSerializer


# Create your views here.

class SubscriptionsListView(generics.ListCreateAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer


class SubscriptionsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsDetailSerializer
    lookup_field = "id"


class SubscriptionsTypeListView(generics.ListAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsTypeSerializer


class SubscriptionsTypeDetailView(generics.RetrieveAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsTypeDetailSerializer
    lookup_field = "id"


class SubscriptionFreezeView(APIView):
    @transaction.atomic
    def post(self, request, id):
        subscription = get_object_or_404(Subscriptions, id=id)
        data = request.data.copy()
        data["subscriptions"] = subscription.id
        data["is_active"] = True
        serializer = SubscriptionsFreezeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        freeze = serializer.save()
        subscription.status = Subscriptions.STATUS_FROZEN
        subscription.save(update_fields=["status", "updated_subscription"])
        return Response(
            SubscriptionsFreezeSerializer(freeze).data,
            status=status.HTTP_201_CREATED,
        )


class SubscriptionUnfreezeView(APIView):
    @transaction.atomic
    def post(self, request, id):
        subscription = get_object_or_404(Subscriptions, id=id)
        subscription.freezes.filter(is_active=True).update(is_active=False)
        subscription.status = Subscriptions.STATUS_ACTIVE
        subscription.save(update_fields=["status", "updated_subscription"])
        return Response(SubscriptionsSerializer(subscription).data)
