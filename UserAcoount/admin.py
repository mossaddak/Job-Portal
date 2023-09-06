from django.contrib import admin
from .models import User, Organization, OrganizationUser, UserRole

# Register your models here.
admin.site.register(User)
admin.site.register(Organization)
admin.site.register(OrganizationUser)


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    model = UserRole
    list_display = ("user", "organization_user", "role")
