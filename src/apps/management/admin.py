from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.management.models import CustomUser
from django.utils.translation import gettext_lazy as _


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Управление ботом'), {'fields': ('bot_manager',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),

    )
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'bot_manager',
    )
    list_editable = (
        'bot_manager',
    )
    list_filter = ('bot_manager', 'is_staff', 'is_superuser', 'is_active', 'groups')
