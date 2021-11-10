from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Права', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Данные', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff',)}
         ),
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'), }),
        ('Права', {
            'classes': ('wide',),
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    readonly_fields = ('last_login',)
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
