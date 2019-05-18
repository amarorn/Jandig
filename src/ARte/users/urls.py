from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import LoginForm
from .views import signup, profile, marker_upload

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.jinja2',
        authentication_form=LoginForm,
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),

    ## deal with password reset
    path('recover/', auth_views.PasswordResetView.as_view(), name='recover'),

    path('markers/upload', marker_upload, name='marker-upload'),
]
