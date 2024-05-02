from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

# class CustomUserManager(BaseUserManager):
#     def create_user(self, phone_number, password=None, **kwargs):
#         if not phone_number:
#             raise ValueError('The Phone Number must be set.')
#
#         user = self.model(phone_number=phone_number, **kwargs)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, phone_number, password=None, **kwargs):
#         kwargs.setdefault('is_staff', True)
#         kwargs.setdefault('is_superuser', True)
#
#         if kwargs.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if kwargs.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self.create_user(phone_number, password, **kwargs)


class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    phone_number = models.CharField(unique=True, max_length=15)
    email = models.EmailField(unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # هش کردن رمز عبور
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone_number


USER = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    bio = models.CharField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
