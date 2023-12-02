from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

# from my_user_profile_app.models import Employee


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# class EmployeeInline(admin.StackedInline):
#     model = Employee
#     can_delete = False
#     verbose_name_plural = "employee"


# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = [EmployeeInline]


# # Re-register UserAdmin
# admin.site.unregister(User)





# UserAdmin.fieldsets += (

#     ("فیلدهای خاص من", {'fields': ('is_author', 'special_user')}),

# )

# Modify the UserAdmin fieldsets
# Convert fieldsets to a list
fieldsets = list(UserAdmin.fieldsets)

# Modify the desired fieldset
fieldsets[2] = (
    _('Permissions'),
    {
        'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'is_author',
            'special_user',
            'groups',
            'user_permissions',
        ),
    },
)

# Convert the list back to a tuple and assign it to UserAdmin.fieldsets
UserAdmin.fieldsets = tuple(fieldsets)


UserAdmin.list_display += ('is_author', 'is_special_user')

# Register the User model with the modified UserAdmin
admin.site.register(User, UserAdmin)