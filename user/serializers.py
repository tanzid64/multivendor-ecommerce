from rest_framework import serializers
from rest_framework.fields import empty
from .models import User
# Rest auth
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
    
class UserLoginSerializer(LoginSerializer):
    username = None
