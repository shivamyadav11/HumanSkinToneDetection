from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    auth_otp = models.CharField(max_length=5)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user
