from django.urls import path
from django.contrib import admin
from django.urls import include
from .views import TrainerAPiView, AdminAPIView, ClientAPIView
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet

router  = DefaultRouter()
router.register(r'client', ClientViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/trainer/', TrainerAPiView.as_view(), name='trainer'),
    path('api/v1/admin/', AdminAPIView.as_view(), name='admin'),
    path('api/v1/client/', ClientAPIView.as_view(), name='client'),
]