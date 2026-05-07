from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Payment
from .serializer import PaymentListSerializer

# Create your views here.

class PaymentListView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializer


class PaymentCreateView(APIView):
    pass
