from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Role

# Customizing the display of CustomUser in the admin panel
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Fields to display in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    # Fields to filter by in the list view
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')
    # Fields for the form view when adding/editing users
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Role Information', {'fields': ('role',)}),
    )
    # Fields for the form view when creating a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'role', 'is_staff', 'is_active'),
        }),
    )
    # Fields for search functionality
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

# Registering the models in the admin panel
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role)