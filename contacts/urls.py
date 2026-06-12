from django.urls import path
from .views import ContactDetailView, ContactListView


urlpatterns = [
    path('api/v1/contacts/', ContactListView.as_view(), name='contacts'),
    path('api/v1/contacts/<int:id>/', ContactDetailView.as_view(), name='contacts-detail'),
]
