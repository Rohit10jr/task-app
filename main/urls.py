from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.list, name='app_list'),
    # path('<int:id>/', views.post, name='app_post'),
    path('form/', views.update, name='app_insert'),
    path('form/<int:id>/', views.update, name='app_update'),
    path('delete/<int:id>/', views.delete, name='app_delete'),
    path('image/', views.show_images, name='show_images'),
    path('upload/<int:id>/', views.upload_image, name='upload_image'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('task/', views.user_task, name='task'),
    path('profile/', views.user_profile, name='profile'),
    path('points/', views.user_points, name='points'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)