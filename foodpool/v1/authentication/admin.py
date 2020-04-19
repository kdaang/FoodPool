from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from foodpool.v1.authentication.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('email',)
    list_filter = ()

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
    )

    search_fields = ('email',)
    ordering = ('email',)

    filter_horizontal = ()


admin.site.register(User, UserAdmin)
