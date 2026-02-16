from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ServiceRequest


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Role Information', {'fields': ('role',)}),
    )


admin.site.register(ServiceRequest)
