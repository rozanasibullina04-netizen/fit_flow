from django.db.models import Sum
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from attendance.models import CheckIn
from bookings.models import Booking
from payments.models import Payment
from subscriptions.models import Subscriptions
from .models import Trainer, Admin, Client
from .serializers import TrainerSerializer, TrainerDetailSerializer, AdminSerializer, AdminUserSerializer, \
    ClientSerializer, AdminSubscriptionListSerializer, AdminSubscriptionUpdateSerializer


class TrainerListView(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class TrainerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerDetailSerializer
    lookup_field = "id"


class AdminListView(generics.ListCreateAPIView):
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
    lookup_field = "id"


class ClientListView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = "id"


class AdminStatsOverviewView(APIView):
    def get(self, request):
        paid_total = Payment.objects.filter(status=Payment.STATUS_PAID).aggregate(
            total=Sum("amount")
        )["total"] or 0
        return Response(
            {
                "clients": Client.objects.count(),
                "trainers": Trainer.objects.count(),
                "active_subscriptions": Subscriptions.objects.filter(
                    status=Subscriptions.STATUS_ACTIVE
                ).count(),
                "bookings": Booking.objects.count(),
                "check_ins": CheckIn.objects.count(),
                "paid_total": paid_total,
            }
        )
