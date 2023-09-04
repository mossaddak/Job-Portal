import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomeUserManager


def upload_to_user_profile_image(instance, filename):
    return f"media/{instance.pk}-{instance.username}/images/profile_image.png"


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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomeUserManager()

    def __str__(self):
        return f"{self.uid}.{self.email}"
