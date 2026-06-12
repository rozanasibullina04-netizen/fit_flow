from rest_framework import generics
from .models import ContactList
from .serializers import ContactListSerializer


class ContactListView(generics.ListCreateAPIView):
    queryset = ContactList.objects.all()
    serializer_class = ContactListSerializer


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactList.objects.all()
    serializer_class = ContactListSerializer
    lookup_field = "id"
