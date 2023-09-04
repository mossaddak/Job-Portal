from django.contrib import admin
from django.urls import path, include

from .views import (
    UserCreate,
    UserLogin,
    PrivateUserprofile,
    PublicOrganizationOnboarding,
)

urlpatterns = [
    path(r"singup", UserCreate.as_view(), name="me.singup"),
    path(r"singin", UserLogin.as_view(), name="me.singin"),
    path(r"me/profile", PrivateUserprofile.as_view(), name="me.singin"),
    path(
        r"organization/onboarding",
        PublicOrganizationOnboarding.as_view(),
        name="me.organization-onboarding",
    ),
]
