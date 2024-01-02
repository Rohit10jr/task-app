from django.contrib import admin
# from django.contrib.auth.models import User
from .models import App, UploadedImage, CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


# class to show the point field on admin page
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


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(App)
admin.site.register(UploadedImage)