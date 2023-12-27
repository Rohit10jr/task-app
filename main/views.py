from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .serializers import AppSerializers
from rest_framework import generics
import json
from django.http import JsonResponse
from .forms import AppForm, ImageForm, RegisterForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import UserProfileForm
# Create your views here.
 
 # rohit 1234 rohit27 124@#jr$abc%
class AppList(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializers

class AppDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializers


@login_required(login_url="/login")
def list(request):
    context = App.objects.all()
    print(context)
    return render(request, 'main/app_list.html', {'context': context})
    # return render(request, 'main/index.html', {'context': context})
    # serializer = AppSerializers(app, many=True)
    # return JsonResponse(serializer.data, safe=False)
        

@login_required(login_url="/login")
@permission_required("main.add_app", login_url="/login", raise_exception=True)
def update(request, id=0):
    if request.method =="GET":
        if id==0:
            form = AppForm()
        else:
            app = App.objects.get(id=id)
            form = AppForm(instance=app)
        return render(request, 'main/app_form.html', {'form': form})
    else:
        if id==0:
            form = AppForm(request.POST, request.FILES)
        else:
            app = App.objects.get(pk=id)
            # print(app)
            # form = ImageForm(request.POST, request.FILES)
            form = AppForm(request.POST, request.FILES, instance=app)
        if form.is_valid():
                form.save()
        return redirect('/app')
    

@login_required(login_url="/login")
@permission_required("main.delete_app", login_url="/login", raise_exception=True)
def delete(request, id):
    # if request.user.has_prem("main.delete_app"):
        app = App.objects.get(pk=id)
        app.delete()
        return redirect('/app/')


def show_images(request):
    images = UploadedImage.objects.all()
    return render(request, 'main/show_images.html', {'images':images})


def upload_image(request, id):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/app')  # Redirect to a success page
    else:
        app = App.objects.get(pk=id)
        form = ImageForm()
        print(app)
    return render(request, 'main/app_post.html', {'form': form, 'app':app})


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user = form.save(commit=False)
            # user.groups.add(2) 
            user_group = Group.objects.get(name='user')
            # user_group.user_set.add(user)
            user.groups.add(user_group)
            login(request, user)
            return redirect('/app')
    else:
        form = RegisterForm()
    return render(request,'registration/signup.html', {'form':form})


def user_logout(request):
    logout(request)
    return redirect('/login')


def user_task(request):
    task = App.objects.all().order_by('-id')[:4]
    # task = App.objects.all().order_by('-created_at')[:3]
    context = {'task': task}
    return render(request, 'main/task.html', context)

@login_required(login_url="/login")
def user_profile(request):
    if request.method == 'POST':
        form  = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'profile has been updated')
            return redirect('profile')
    else:
        form =UserProfileForm(instance=request.user)
    return render(request, 'registration/profile.html', {'form':form})
    # if request.user.is_authenticated:
    #     context = request.user
    #     return render(request, 'registration/profile.html', {'context':context})
    
        # username = request.user.username
        # firstname = request.user.first_name
        # lastname = request.user.last_name
        # email = request.user.email
        # context = {'username': username, 'email': email, 'firstname':firstname, 'lastname':lastname, 'email': email}
        # return render(request, 'registration/profile.html', context)


def user_points(request):
    if request.user.is_authenticated:
        context = request.user
        return render(request, 'main/points.html', {'context':context})
