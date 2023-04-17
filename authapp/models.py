from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=15, unique=False)
    email = models.EmailField(max_length=100, unique=True)
