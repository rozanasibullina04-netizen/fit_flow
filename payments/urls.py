from django.urls import path
from .views import PaymentCreateView, PaymentListView

urlpatterns = [
    # path("/api/v1/payments-create/", PaymentCreateView.as_view(), name="payments-create"),
    path("/api/v1/payments-list/", PaymentListView.as_view(), name="payments-list")
]