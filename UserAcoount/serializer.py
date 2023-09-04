from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .utils import TokenHelper
from .models import Organization, OrganizationUser

User = get_user_model()


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uid",
            "first_name",
            "last_name",
            "username",
            "email",
            "date_joined",
            "last_login",
            "password",
        ]

        read_only_fields = ("date_joined", "last_login")

    def create(self, validated_data, *args, **kwargs):
        password = validated_data["password"]

        user = User.objects.create(
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            username=validated_data["username"],
            email=validated_data["email"].lower(),
        )
        user.set_password(password)
        user.save()
        return validated_data


class UserAccountLoginSerializer(serializers.Serializer):
    email = serializers.SlugRelatedField(
        queryset=User.objects.filter(), slug_field="email", write_only=True
    )
    password = serializers.CharField(write_only=True)
    refresh = serializers.CharField(max_length=255, read_only=True)
    access = serializers.CharField(max_length=255, read_only=True)

    def create(self, validated_data):
        user = validated_data.get("email")
        password = validated_data.get("password")

        # Check password
        if not user.check_password(password):
            raise AuthenticationFailed()

        # Get the tokens
        (
            validated_data["refresh"],
            validated_data["access"],
        ) = TokenHelper().create_token(user)

        return validated_data


class PrivateUserProfile(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            "uid",
            "first_name",
            "last_name",
            "username",
            "email",
            "date_joined",
            "last_login",
            "password",
        ]

        read_only_fields = ("date_joined", "last_login")

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        if password:
            validated_data["password"] = make_password(password)
        return super().update(instance, validated_data)


class PublicOrganizationUserOnboarding(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=4, max_length=50, write_only=True)
    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=50)
    organization_name = serializers.CharField(min_length=2, max_length=50)

    def validate_email(self, data):
        email = data.lower()
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with email already exists!")
        return data

    def create(self, validated_data, *args, **kwargs):
        email = validated_data["email"].lower()
        password = validated_data["password"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        organization_name = validated_data["organization_name"]

        user = User.objects.create(
            email=email,
            username=email,
            first_name=first_name,
            last_name=last_name,
            is_active=True,
        )

        user.set_password(password)
        user.save()
        # Create organization
        organization = Organization.objects.create(name=organization_name)
        # Create organization user
        organization.add_owner(user)
        return validated_data
