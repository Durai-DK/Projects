from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import logout
from rest_framework import generics
from .serializers import *
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .permissions import *


class StudentListView(generics.ListCreateAPIView):

    queryset = Student.objects.all()
    serializer_class = Student_Serializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RegisterApi(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = User_Serializer

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)

        data = {
                'id': serializer.data['id'],
                'Name': serializer.data['username'],
                'password': serializer.data['password'],
                'token': token.key
                }
        return Response(data, status=200)


class LoginApi(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = User_Serializer

    permissions = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user)

        data = {
            'id': serializer.data['id'],
            'Name': serializer.data['username'],
            'password': serializer.data['password'],
            'token': token.key
        }
        return Response(data)


class LogoutApi(generics.GenericAPIView):

    def get(self, request):
        logout(request)
        return Response('Logout Successfully')


class ChangePasswordAPI(generics.UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):

        user = self.request.user
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            if check_password(old_password, user.password):

                user.set_password(new_password)
                user.save()

                return Response({'Success': 'New Password change Successfully'}, status=200)

            else:
                return Response({'error': 'Old Password is Invaild'}, status=400)

        else:
            return Response(serializer.errors, status=400)


class ForgotPasswordAPI(APIView):

    def post(self, request):
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

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

        return Response({'message': 'Password reset email sent'}, status=200)
