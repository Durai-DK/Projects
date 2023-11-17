from django.contrib import admin
from django.urls import path
from .views import RegisterAPI, LoginAPI, LogoutAPI, ProtectedAPI, ChangePasswordAPI, ForgotPasswordAPI


urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    path('protected/', ProtectedAPI.as_view(), name='protected'),
    path('change-password/', ChangePasswordAPI.as_view(), name='change_password'),
    path('forgot-password/', ForgotPasswordAPI.as_view(), name='forgot_password'),
    # path('reset-password/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

