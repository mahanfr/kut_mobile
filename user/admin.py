from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User

# Extending user admin class
class UserConfig(UserAdmin):
    model = User
    search_fields = ('email','first_name','last_name','phone_number')
    list_filter = ('is_active','is_staff','is_superuser')
    ordering = ('-created_at',)
    list_display = ('email','first_name','last_name','phone_number','is_active','is_staff')

    fieldsets = (
        (None, {'fields': ('email','phone_number',)}),
        ('Permissions', {'fields': ('is_staff','is_superuser', 'is_active')}),
    )
    # This is used for creating a new user in admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','phone_number','first_name','last_name','password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

# Register your models here.
admin.site.register(User,UserConfig)