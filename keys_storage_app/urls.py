from rest_framework import routers
from django.urls import path, include
from .views import (
    KeyAPIView,
    KeyDetailAPIView,
)

urlpatterns = [
    path('key_storage/', KeyAPIView.as_view(), name='key_storage'),
    path('key_detail/', KeyDetailAPIView.as_view(), name='key_detail'),
]

