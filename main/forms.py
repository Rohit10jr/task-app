from django import forms 
from .models import App, UploadedImage, CustomUser
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ('__all__')
        labels = {  
                'appicon' : 'App icon',
                'appname' : 'App Name',
                'link' : 'App Link',
                'category' : 'App Category',
                'subcategory' : 'Sub Category',
                'points' : 'App Points',
                }

class ImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ('image',)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'