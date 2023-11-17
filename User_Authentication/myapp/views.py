from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import *


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


class UserRegistrationView(APIView):
    def post(self, request, formate=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token': token, 'meg': 'Registration Success'}, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)

            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token': token, "meg": "Login Success"}, status=status.HTTP_200_OK)

            else:
                return Response({"errors": {"non_field_errors": ["Email or Password is not valid"]}},
                                status=status.HTTP_404_NOT_FOUND)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, formate=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, formate=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user': request.user})

        if serializer.is_valid(raise_exception=True):
            return Response({'meg': "Password Changed Successfully"}, status= status.HTTP_200_OK)


class SendPasswordResetEmailView(APIView):

    def post(self, request, formate=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            return Response({"meg": "Password Reset Link Send. kindly check your Email"}, status=status.HTTP_200_OK)


class UserPasswordResetView(APIView):

    def post(self, request, uid, token):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid': uid, "token": token})

        if serializer.is_valid(raise_exception=True):
            return Response({'meg': "Password Reset Successfully"}, status=status.HTTP_200_OK)


class ResgisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"meg": "Registration Successfull"})
