from django.db import models
from core.models import TimeStampMixin
from user.models import User
# Create your models here.

class AuthorProfile(TimeStampMixin):
    user = models.OneToOneField(User, related_name="author_profile", on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    dob = models.DateField()
    description = models.TextField()
    is_verified = models.BooleanField(default=False)

# Making a follower option so that user can follow author
class AuthorFollower(TimeStampMixin):
    user = models.OneToOneField(User, related_name="follower", on_delete=models.CASCADE)
    author = models.OneToOneField(AuthorProfile, related_name="follower", on_delete=models.CASCADE)
    