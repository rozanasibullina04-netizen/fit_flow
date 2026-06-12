from rest_framework import generics

from .models import Payment
from .serializers import PaymentListSerializer


class PaymentListView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializer


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializer
    lookup_field = "id"
