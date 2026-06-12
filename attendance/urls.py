from django.urls import path
from .views import (
    AdminVisitHistoryView,
    CheckInDetailView,
    CheckInView,
    VisitHistoryDetailView,
    VisitHistoryView,
)

urlpatterns = [
    path('api/v1/visit-history/', VisitHistoryView.as_view(), name='visit-history'),
    path('api/v1/visit-history/<int:id>/', VisitHistoryDetailView.as_view(), name='visit-history-detail'),
    path('api/v1/admin/visit-history/', AdminVisitHistoryView.as_view(), name='admin-visit-history'),
    path('api/v1/check-ins/', CheckInView.as_view(), name='check-ins'),
    path('api/v1/check-ins/<int:id>/', CheckInDetailView.as_view(), name='check-ins-detail'),
]
