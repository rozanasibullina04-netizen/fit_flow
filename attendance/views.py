from rest_framework import generics
from .models import CheckIn, VisitHistory
from .serializers import AdminVisitHistorySerializer, CheckInSerializer, VisitHistorySerializer


class VisitHistoryView(generics.ListAPIView):
    queryset = VisitHistory.objects.all()
    serializer_class = VisitHistorySerializer


class AdminVisitHistoryView(generics.ListCreateAPIView):
    queryset = VisitHistory.objects.all()
    serializer_class = AdminVisitHistorySerializer


class VisitHistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VisitHistory.objects.all()
    serializer_class = VisitHistorySerializer
    lookup_field = "id"


class CheckInView(generics.ListCreateAPIView):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer


class CheckInDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer
    lookup_field = "id"
