from django.contrib import admin
from .models import User,UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ("email","first_name","last_name","username","is_active")
    ordering = ("-date_joined",)
    filter_horizontal = ('groups', 'user_permissions',)
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ( 'groups', 'user_permissions')}),
    )

admin.site.register(User,CustomUserAdmin)
admin.site.register(UserProfile)