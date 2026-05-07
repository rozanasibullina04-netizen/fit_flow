from django.urls import path
from .views import VisitHistoryView, AdminVisitHistoryView

urlpatterns = [
    path('api/v1/visit-history/', VisitHistoryView.as_view(), name='visit-history'),
    path('api/v1/admin/visit-history/', AdminVisitHistoryView.as_view(), name='admin-visit-history'),
]