from django.urls import path
from .views import *


urlpatterns = [

    path('register/', RegistrationView.as_view(), name="Register"),
    path('login/', LoginView.as_view(), name='Login'),
]
