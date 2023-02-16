from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    KeyAPIView,
    KeyDetailAPIView,
    ShareAPIView,
    KeyDetailDecryptedAPIView,
)


urlpatterns = [
    path('v1/key_storage/',
         KeyAPIView.as_view(), name='key_storage'),
    path('v1/key_detail/<int:key_id>/',
         KeyDetailAPIView.as_view(), name='key_detail'),
    path('v1/share_email/<int:key_id>/',
         ShareAPIView.as_view(), name='sharing_email'),
    path('v1/key_detail/decrypted/<int:key_id>/email_id/<int:email_id>/',
         KeyDetailDecryptedAPIView.as_view(), name='key_decrypted'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

