from django.urls import path
from .views import VisitHistoryView


urlpatterns = [
    path('api/v1/visit-history/', VisitHistoryView.as_view(), name='visit-history')
]