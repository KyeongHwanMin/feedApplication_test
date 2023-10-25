from django.urls import path

from accounts.views import UserAPIView, UserVerificationView

urlpatterns = [
    path("", UserAPIView.as_view(), name="user"),
    path("verification", UserVerificationView.as_view(), name="user-verification"),
]
