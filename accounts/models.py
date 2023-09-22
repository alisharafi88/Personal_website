from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile = models.ImageField(upload_to='covers/users', blank=True, null=True)
