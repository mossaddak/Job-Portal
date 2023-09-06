from typing import Optional

from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from ..models import User, Organization, OrganizationUser, UserRole

from ..choices import (
    OrganizationStatus,
    OrganizationUserRole,
    OrganizationUserStatus,
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

    def get_user_by_email(self, email: str) -> User:
        return get_object_or_404(User, email=email)


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
        status: OrganizationUserStatus.values = OrganizationUserStatus.ACTIVE,
        is_default: bool = False,
    ) -> OrganizationUser:
        return OrganizationUser.objects.create(
            organization=organization,
            user=user,
            status=status,
            is_default=is_default,
        )

    def create_user_role(
        self,
        user: User,
        role: str,
        organization_user: Optional[OrganizationUser] = None,
    ) -> UserRole:
        return UserRole.objects.create(
            user=user, role=role, organization_user=organization_user
        )
