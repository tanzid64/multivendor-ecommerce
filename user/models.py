from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from .managers import UserManager
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_mod = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)