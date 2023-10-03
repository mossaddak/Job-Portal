from django.core.management.base import BaseCommand

from common import color

from ...choices import OrganizationUserRole
from ...services.users import UserService, OrganizationService
from ...models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Create user
        try:
            user = User.objects.create_user(
                email="mossaddak@gmail.com",
                password="123456",
                first_name="Mossaddak",
                last_name="Sium",
                is_staff=True,
                is_superuser=True,
                is_active=True,
            )
            print(f"{color.GREEN} successfully user created {color.RESET}")

            # Create organization
            organization = OrganizationService.create_organization(
                self, name="Mossaddak ORG-1"
            )
            print(f"{color.GREEN} successfully organization created {color.RESET}")

            # Create organization user
            organization_user = OrganizationService.create_organization_user(
                self, organization, user
            )
            print(f"{color.GREEN} successfully organization user created {color.RESET}")

            # Create organization user role
            OrganizationService.create_user_role(
                self, user, OrganizationUserRole.OWNER, organization_user
            )
            print(f"{color.GREEN} successfully organization role created {color.RESET}")
        except Exception as e:
            print(f"{color.RED} Error: {e} {color.RESET}")
