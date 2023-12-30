from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# from django.contrib.auth import get_user_model

# Create your models here.
class App(models.Model):
    appicon = models.ImageField(upload_to='icon/')
    appname = models.CharField(max_length=255)
    link = models.CharField(max_length=100)
    category= models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.appname
    
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    

class CustomUser(AbstractUser):
    point = models.IntegerField(default=0)
    
