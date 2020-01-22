from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from user_model.models import UserModel, UserRole, Tag


class UserModelAdmin(UserAdmin):
    list_display = ('username', 'fullname', 'role', 'last_login', 'is_active', 'is_admin', 'is_staff')
    search_fields = ('username', 'fullname', 'role')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.unregister(Group)
admin.site.register(UserModel, UserModelAdmin)
admin.site.register(UserRole)
admin.site.register(Tag)
