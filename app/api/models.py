from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager

from django.contrib import admin

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # username = models.CharField(max_length=7, unique=True, db_index=True, primary_key=True)
    id = models.CharField(primary_key=True, editable=False, max_length=7, unique=True, db_index=True)
    auth_id = models.CharField(max_length=16)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)

    USERNAME_FIELD = "id"
    REQUIRED_FIELDS = ["auth_id", "first_name", "last_name", "email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.id
    