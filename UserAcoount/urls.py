from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path(r"singup", views.UserCreate.as_view(), name="me.singup"),
    path(r"singin", views.UserLogin.as_view(), name="me.singin"),
    path(r"me/profile", views.PrivateUserprofile.as_view(), name="me.singin"),
    path(
        r"organization/onboarding",
        views.PublicOrganizationOnboarding.as_view(),
        name="me.organization-onboarding",
    ),
    path(
        r"organization/user",
        views.PrivateOrganizationUser.as_view(),
        name="me.organization-hr",
    ),
]
