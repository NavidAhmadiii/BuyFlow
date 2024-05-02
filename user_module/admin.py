from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.

# @admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('phone_number', 'email', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('phone_number', 'email',)
    ordering = ('phone_number',)


admin.site.register(CustomUser, CustomUserAdmin)
