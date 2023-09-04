import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q, UniqueConstraint

from .managers import CustomeUserManager
from .choices import (
    OrganizationStatus,
    OrganizationUserRole,
    OrganizationUserStatus,
    UserStatus,
)


def upload_to_user_profile_image(instance, filename):
    return f"media/{instance.pk}-{instance.username}/images/profile_image.png"


def upload_to_organization_image(instance, filename):
    return f"media/{instance.id}-{instance.name}/images/organization_profile_image.png"


# Create your models here.
class User(AbstractUser):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(
        max_length=50,
        unique=True,
        null=False,
        error_messages={"unique": "the email must be unique"},
    )
    is_applicant = models.BooleanField(default=False)
    image = models.ImageField(upload_to=upload_to_user_profile_image, null=True)

    status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        db_index=True,
        default=UserStatus.ACTIVE,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomeUserManager()

    def __str__(self):
        return f"{self.uid}.{self.email}"

    def get_name(self):
        name = f"{self.first_name} {self.last_name}"
        return name.strip()


class Organization(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to_organization_image, null=True)
    status = models.CharField(
        max_length=20,
        choices=OrganizationStatus.choices,
        db_index=True,
        default=OrganizationStatus.DRAFT,
    )

    def __str__(self):
        return f"Name: {self.name}, Uid: {self.uid}, Status: {self.status}"

    def add_hr(self, user, is_default: bool = False):
        return OrganizationUser.objects.create(
            organization=self,
            user=user,
            role=OrganizationUserRole.HR,
            status=OrganizationUserStatus.ACTIVE,
            is_default=is_default,
        )

    def add_owner(self, user: User, is_default: bool = False):
        return OrganizationUser.objects.create(
            organization=self,
            user=user,
            role=OrganizationUserRole.OWNER,
            status=OrganizationUserStatus.ACTIVE,
            is_default=is_default,
        )


class OrganizationUser(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(
        choices=OrganizationUserRole.choices,
        max_length=20,
    )
    status = models.CharField(
        max_length=20,
        choices=OrganizationUserStatus.choices,
        default=OrganizationUserStatus.PENDING,
    )
    is_default = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["user"],
                condition=Q(is_default=True),
                name="user_have_one_default_organization",
                violation_error_message="A merchant can have only one default organization.",
            )
        ]

    def __str__(self):
        return f"ID: {self.id}, Org: {self.organization}, User: {self.user}, Role: {self.role}, Status: {self.status}"
