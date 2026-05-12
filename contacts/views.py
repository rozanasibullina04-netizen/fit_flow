from rest_framework import generics
from .models import ContactList
from .serializers import ContactListSerializer


class ContactListView(generics.ListAPIView):
    queryset = ContactList.objects.all()
    serializer_class = ContactListSerializer