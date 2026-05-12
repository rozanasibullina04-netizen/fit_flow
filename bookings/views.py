from rest_framework import generics
from rest_framework.views import APIView
from .models import WaitingList, Booking
from .serializers import WaitingListSerializer, BookingSerializer


class WaitingListView(generics.ListAPIView):
    queryset = WaitingList.objects.all()
    serializer_class = WaitingListSerializer


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingWaitAPIView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingCancelView(APIView):
    pass


class BookingWaitlistView(APIView):
    pass
