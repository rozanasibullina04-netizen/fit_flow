from rest_framework import generics
from .models import WaitingList, Booking
from .serializers import WaitingListSerializer, BookingSerializer


class WaitingListView(generics.ListCreateAPIView):
    queryset = WaitingList.objects.all()
    serializer_class = WaitingListSerializer


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = "id"


class BookingWaitAPIView(generics.ListCreateAPIView):
    serializer_class = WaitingListSerializer

    def get_queryset(self):
        return WaitingList.objects.filter(training_id=self.kwargs["training_id"])

    def perform_create(self, serializer):
        serializer.save(training_id=self.kwargs["training_id"])
