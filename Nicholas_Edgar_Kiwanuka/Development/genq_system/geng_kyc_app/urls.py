from django.urls import path
from . import views


urlpatterns = [
    path("", views.kyc_registration, name="kyc-registration"),
    path("success/", views.success, name="success"),
]
