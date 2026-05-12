from django.urls import path
from .views import ContactListView


urlpatterns = [
    path("/api/v1/contacts/", ContactListView.as_view(), name="contacts")
]