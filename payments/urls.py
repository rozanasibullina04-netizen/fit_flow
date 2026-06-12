from django.urls import path

from .views import PaymentDetailView, PaymentListView


urlpatterns = [
    path("api/v1/payments/", PaymentListView.as_view(), name="payments"),
    path("api/v1/payments/<int:id>/", PaymentDetailView.as_view(), name="payments-detail"),
]
