from django import forms 
from .models import App, UploadedImage, CustomUser
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AppForm(forms.ModelForm):
    
        class Meta:
            model = App
            fields = ('__all__')

        def __init__(self, *args, **kwargs):
            super(AppForm, self).__init__(*args, **kwargs)

            defualt_image_path = '/media/photo.png'
            self.fields['appicon'].widget.attrs['placeholder'] = defualt_image_path
            self.fields['appicon'].widget.attrs['classs']= 'appicon-field'
            self.fields['appname'].widget.attrs.update({'placeholder': 'Apps Name', 'class':'appname-field'})
            self.fields['link'].widget.attrs.update({'placeholder':'App Link','class':'link-field'})
            self.fields['category'].widget.attrs.update({'placeholder':'App Category', 'class': 'catg-field'})
            self.fields['subcategory'].widget.attrs.update({'placeholder':'Sub Category', 'class': 'subcatg-field'})
            self.fields['points'].widget.attrs.update({'placeholder':'ADD POINTS', 'class': 'points-field'})



        # labels = {  
        #         'appicon' : 'App icon',
        #         'appname' : 'App Name',
        #         'link' : 'App Link',
        #         'category' : 'App Category',
        #         'subcategory' : 'Sub Category',
        #         'points' : 'App Points',
        #         }

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