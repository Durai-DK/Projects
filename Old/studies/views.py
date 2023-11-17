from rest_framework import generics
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from knox.views import LogoutView
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({'user': UserSerializer(user).data, 'token': token})


class LoginAPI(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)
        return Response({'user': UserSerializer(user).data, 'token': token})


class LogoutAPI(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)



class ProtectedAPI(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        return Response({'message': f'Hello, {user.username}! This is a protected API endpoint.'})
    

@csrf_exempt
def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                from_email='your_email@example.com',  # Set your email address here
                email_template_name='password_reset_email.html',  # Create a template for the email
            )
            return JsonResponse({'message': 'Password reset email sent'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    

class ChangePasswordAPI(APIView):


    def put(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        # Check if the old password matches the user's current password
        if not check_password(old_password, user.password):
            return Response({'error': 'Old password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)

        # Change the user's password
        user.set_password(new_password)
        user.save()

        return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)
    

class ForgotPasswordAPI(APIView):
    def post(self, request):
        email = request.data.get('email')

        # Find the user with the provided email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Generate a password reset token
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        # Build the password reset URL
        reset_url = f"http://localhost:8000/api/accounts/reset-password/{uid}/{token}"

        # Send the password reset email
        email_subject = 'Password Reset'
        email_body = render_to_string('password_reset_email.html', {'reset_url': reset_url})
        email = EmailMessage(subject=email_subject, body=email_body, to=[email])
        email.send()

        return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)