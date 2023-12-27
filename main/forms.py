from django import forms 
from .models import App, UploadedImage, CustomUser
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from crispy_forms.helper import FormHelper

class AppForm(forms.ModelForm):
    
        class Meta:
            model = App
            fields = ('__all__')

        def __init__(self, *args, **kwargs):
            super(AppForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_show_labels = False

            # defualt_image_path = '/media/photo.png'
            # self.fields['appicon'].widget.attrs['placeholder'] = defualt_image_path
            self.fields['appicon'].widget.attrs['class']= 'appicon-field'
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

    
    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)

        self.fields['image'].widget.attrs['class']= 'uploadimage-field'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

        self.fields['username'].widget.attrs.update({'placeholder': 'User Name', 'class':'Username-field'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email','class':'email-field'})
        self.fields['first_name'].widget.attrs.update({'placeholder':'First Name', 'class': 'fname-field'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'Last Name', 'class': 'lnmae-field'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password 1', 'class': 'pass1-field'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Password 2', 'class': 'pass2-field'})


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {
            'username': None,
            }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

        self.fields['username'].widget.attrs['class']= 'userprofile'
        self.fields['email'].widget.attrs['class']= 'emailprofile'
        self.fields['first_name'].widget.attrs['class']= 'fnameprofile'
        self.fields['last_name'].widget.attrs['class']= 'lnameprofile'