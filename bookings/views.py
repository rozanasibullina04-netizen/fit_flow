from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from .models import Booking
from .serializers import BookingListSerializer

# Create your views here.

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer

class BookingWaitAPIView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer


class BookingCanselView(APIView):
    pass


class BookingWaitlistView(APIView):
    pass
