from django.urls import path
from .views import *


urlpatterns = [

    path('registers', RegisterApi.as_view(), name='register'),
    path('login', LoginApi.as_view(), name='login'),
    path('logout', LogoutApi.as_view(), name='logout'),
    path('change-password', ChangePasswordAPI.as_view(), name='change_password'),
    path('forget-password', ForgotPasswordAPI.as_view(), name='forget_password'),
    path('studentlist', StudentListView.as_view())
]
