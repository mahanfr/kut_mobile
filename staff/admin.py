from django.contrib import admin
from staff.models import Staff,StaffGroup,StaffInstitute

class StaffConfig(admin.ModelAdmin):
    model = Staff
    search_fields = ('first_name','last_name','responsibility','group','institute')
    ordering = ('last_name',)
    list_display = ('first_name','last_name','responsibility','group','institute')

    fieldsets = (
        (None, {'fields': ('first_name','last_name','responsibility','group','institute')}),
        ('Optionals', {'fields': ('profile_image','email','internal_phone_line','education','date_joind')}),
    )
    # This is used for creating a new model in admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','responsibility','group','institute',
                'profile_image','email','internal_phone_line','education','date_joind')}
         ),
    )


admin.site.register(Staff,StaffConfig)
admin.site.register(StaffGroup)
admin.site.register(StaffInstitute)
