from typing import Any
from django.shortcuts import render, redirect
from .serializers import UserLoginSerializer
from .models import User
from .utils import send_registration_email
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView
# Rest Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# Token
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes

# All auth
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView


class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://localhost:8000/accounts/~redirect'
    client_class = OAuth2Client

class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False
    def get_redirect_url(self):
        return 'redirect-url'

#JWT Token Generator Method
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password']

            user = authenticate(email=email, password=password)
            if user:
                token = get_tokens_for_user(user)
                return Response (
                    {'token': token, 'message': "Login successfull"}, 
                    status=status.HTTP_200_OK
                )
            # if user doesn't exist
            return Response(
                {'error': 'Email or password is incorrect'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.errors)

