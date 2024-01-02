from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

# model for app 
class App(models.Model):
    CATEGORY_CHOICES = [
        ('Social', 'Social'),
        ('Finance', 'Finance'),
        ('Shopping', 'Shopping'),
        ('Communication', 'Communication'),
        ('Travel', 'Travel'),
        ('Entrainment', 'Entrainment'),
        ('Productivity', 'Productivity'),
        ('Music', 'Music'),
        ('Strategy', 'Strategy'),
        ('Puzzle', 'Puzzle'),
    ]

    SUBCATEGORY_CHOICES = [
        ('Network', 'Network'),
        ('Digital', 'Digital'),
        ('Messaging', 'Messaging'),
        ('Audio', 'Audio'),
        ('Marketplace', 'Marketplace'),
        ('Action', 'Action'),
        ('Streaming', 'Streaming'),
        ('Loans', 'Loans'),
        ('Sharing', 'Sharing'),
        ('Offline', 'offline'),
    ]
    appicon = models.ImageField(upload_to='icon/')
    appname = models.CharField(max_length=255)
    link = models.CharField(max_length=100)
    category= models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    subcategory = models.CharField(max_length=100, choices=SUBCATEGORY_CHOICES)
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.appname

# models for user upload    
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    
# user model 
class CustomUser(AbstractUser):
    point = models.IntegerField(default=0)
    
