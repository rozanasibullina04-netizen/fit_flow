from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from .models import VisitHistory
from .serializers import VisitHistorySerializer

# Create your views here.

class VisitHistoryView(generics.ListAPIView):
    queryset = VisitHistory.objects.all()
    serializer_class = VisitHistorySerializer


class QRCodeView(APIView):
    pass


class CheckInView(APIView):
    pass


class CheckInTimeView(APIView):
    pass