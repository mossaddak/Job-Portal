from django.contrib import admin
from django.urls import path, include

from .views import (
    UserCreate,
    UserLogin,
    PrivateUserprofile,
    PublicOrganizationOnboarding,
    PrivateOrganizationUser,
    PublicUserList1,
    PublicUserList2,
    PublicUserList3
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
    path(
        r"organization/user",
        PrivateOrganizationUser.as_view(),
        name="me.organization-hr",
    ),
    path(
        r"users1",
        PublicUserList1.as_view(),
        name="public.user1-list",
    ),
    path(
        r"users2",
        PublicUserList2.as_view(),
        name="public.user2-list",
    ),
    path(
        r"users3",
        PublicUserList3.as_view(),
        name="public.user3-list",
    ),
]
