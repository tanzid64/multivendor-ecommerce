from django.contrib import admin
from .models import AuthorFollower, AuthorProfile
# Register your models here.
admin.site.register(AuthorProfile)
admin.site.register(AuthorFollower)