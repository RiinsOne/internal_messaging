from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from user_model.models import UserModel


class UserModelAdmin(UserAdmin):
    list_display = ('username', 'fullname', 'entity', 'last_login', 'is_active', 'is_admin', 'is_staff')
    search_fields = ('username', 'fullname', 'entity')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(UserModel, UserModelAdmin)
admin.site.unregister(Group)
