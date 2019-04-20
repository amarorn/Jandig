from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import service_worker, index, upload_image, login, signup, create_exhibition



urlpatterns = [
    path('', index, name='index'),
    
    path('sw.js', service_worker, name='sw'),
    path('upload', upload_image, name='upload-image'),

    path('accounts/login', login, name='login'),
    path('accounts/signup', signup, name='signup'),

    path('create-exhibition', create_exhibition, name='create-exhibition'),

]
