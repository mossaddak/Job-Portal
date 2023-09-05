from rest_framework.exceptions import ValidationError

from ..models import User, Organization, OrganizationUser

from ..choices import (
    OrganizationStatus,
    OrganizationUserRole,
    OrganizationUserStatus,
    UserStatus,
)


class UserHelper:
    def create_user(
        self,
        email: str,
        password: str,
        first_name: str = "",
        last_name: str = "",
    ) -> User:
        return User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

    def get_user_by_phone(self, email: str) -> User:
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError({"detail": "User cannot found."})


class OrganizationHelper:
    def create_organization(
        self,
        name: str,
        status: OrganizationStatus.values = OrganizationStatus.ACTIVE,
    ) -> Organization:
        return Organization.objects.create(name=name, status=status)

    def create_organization_user(
        self,
        organization: Organization,
        user: User,
        role: OrganizationUserRole.values = OrganizationUserRole.OWNER,
        status: OrganizationUserStatus.values = OrganizationUserStatus.ACTIVE,
        is_default: bool = False,
    ) -> OrganizationUser:
        return OrganizationUser.objects.create(
            organization=organization,
            user=user,
            role=role,
            status=status,
            is_default=is_default,
        )
