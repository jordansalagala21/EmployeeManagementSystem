from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.TextField(blank=True, help_text="A comma-separated list of permissions")

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    # Add related_name to avoid conflicts with the default User model
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Change this to avoid conflict
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_user_permissions",  # Change this to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name="customuser",
    )