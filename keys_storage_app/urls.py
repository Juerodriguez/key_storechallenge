from rest_framework import routers
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    KeyAPIView,
    KeyDetailAPIView,
    ShareAPIView,
)

sharing_email = ShareAPIView.as_view()

urlpatterns = [
    path('v1/key_storage/', KeyAPIView.as_view(), name='key_storage'),
    path('v1/key_detail/<int:key_id>/', KeyDetailAPIView.as_view(), name='key_detail'),
    path('v1/share_email/<int:key_id>/', sharing_email, name='sharing_email'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

