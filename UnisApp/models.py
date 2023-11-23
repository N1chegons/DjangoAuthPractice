from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(null=False, blank=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(default='img/logo-profile.jpg')

    def __str__(self):
        return str(self.user)
