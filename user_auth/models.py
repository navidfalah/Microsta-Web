from django.db import models
from django.contrib.auth.models import AbstractUser
from user_auth.emailusermanager import EmailUserManager


class User(AbstractUser):
    username = None
    email = models.CharField(max_length=50, unique=True)

    objects = EmailUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    backend = 'user_auth.emailbackend.EmailBackend'
