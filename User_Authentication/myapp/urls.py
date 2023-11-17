from django.urls import path
from .views import *

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name='register'),
    path("login/", UserLoginView.as_view(), name="Login"),
    path("profile/", UserProfileView.as_view(), name="Profile"),
    path("change_password/", UserChangePasswordView.as_view(), name="Change-Password"),
    path("send_password_reset_email/", SendPasswordResetEmailView.as_view(), name="send-password-reset-email"),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='Reset-Password'),
    path('regis/', ResgisterView.as_view())
]
