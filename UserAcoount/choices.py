from django.db import models


class OrganizationStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PLACEHOLDER = "PLACEHOLDER", "Placeholder"
    PENDING = "PENDING", "Pending"
    ACTIVE = "ACTIVE", "Active"
    HIDDEN = "HIDDEN", "Hidden"
    REMOVED = "REMOVED", "Removed"


class OrganizationUserRole(models.TextChoices):
    OWNER = "OWNER", "Owner"
    ADMIN = "ADMIN", "Admin"
    HR = "HR", "Human Resource"
    APPLICANT = "APPLICANT", "Applicant"


class OrganizationUserStatus(models.TextChoices):
    INVITED = "INVITED", "Invited"
    PENDING = "PENDING", "Pending"
    ACTIVE = "ACTIVE", "Active"
    SUSPEND = "SUSPEND", "Suspend"
    REJECTED = "REJECTED", "Rejected"
    DEACTIVATE = "DEACTIVATE", "Deactivate"
    HIDDEN = "HIDDEN", "Hidden"
    REMOVED = "REMOVED", "Removed"

class UserStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PLACEHOLDER = "PLACEHOLDER", "Placeholder"
    ACTIVE = "ACTIVE", "Active"
    HIDDEN = "HIDDEN", "Hidden"
    PAUSED = "PAUSED", "Paused"
    REMOVED = "REMOVED", "Removed"
