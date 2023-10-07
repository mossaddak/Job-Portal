from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from django.contrib.auth import get_user_model


from .serializer import (
    UserAccountSerializer,
    UserAccountLoginSerializer,
    PrivateUserProfile,
    PublicOrganizationUserOnboarding,
    PrivateOrganizationUserSerializer,
)

User = get_user_model()


# Create your views here.
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserAccountSerializer
    permission_classes = [AllowAny]


class UserLogin(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserAccountLoginSerializer


class PrivateUserprofile(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PrivateUserProfile

    def get_object(self):
        return get_object_or_404(User, email=self.request.user.email)


class PublicOrganizationOnboarding(generics.CreateAPIView):
    serializer_class = PublicOrganizationUserOnboarding
    permission_classes = [AllowAny]


class PrivateOrganizationUser(generics.CreateAPIView):
    serializer_class = PrivateOrganizationUserSerializer
    permission_classes = [IsAuthenticated]


from django.db.models import Q
from django.db.models import Case, Value, BooleanField, When, F, ExpressionWrapper, fields



class PublicUserList1(generics.ListAPIView):
    serializer_class = UserAccountSerializer
    queryset = User.objects.filter(is_active=True).order_by("first_name")
    permission_classes = [AllowAny]

    def get_queryset(self):
        return self.queryset.filter(first_name="") | self.queryset.filter(last_name="")


class PublicUserList2(generics.ListAPIView):
    serializer_class = UserAccountSerializer
    queryset = User.objects.filter(is_active=True).order_by("first_name")

    def get_queryset(self):
        return self.queryset.filter(Q(first_name="") | Q(last_name="")).order_by(
            "first_name" 
        )


class PublicUserList3(generics.ListAPIView):
    serializer_class = UserAccountSerializer
    queryset = (
        User.objects.filter(is_active=True)
        .annotate(
            has_empty_name=ExpressionWrapper(
                Case(
                    When(Q(first_name="") | Q(last_name=""), then=Value(True)),
                    default=Value(False),
                    output_field=BooleanField(),
                ),
                output_field=fields.BooleanField(),
            )
        )
        .order_by("first_name")
    )

    def get_queryset(self):
        return self.queryset.filter(has_empty_name=True).order_by("first_name")



