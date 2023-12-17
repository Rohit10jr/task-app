from django.contrib import admin
# from django.contrib.auth.models import User
from .models import App, UploadedImage, CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'email', 'point', 'is_active', 'is_staff')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Other Personal info',
            {
                'fields': (
                    'point',
                )
            }
        )
    )

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(App)
admin.site.register(UploadedImage)