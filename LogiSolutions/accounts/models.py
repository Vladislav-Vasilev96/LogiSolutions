from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models

from LogiSolutions.core.model_mixins import Gender


class CustomUserHandler(BaseUserManager):
    def create_user(self, username, email=None, password=None, is_staff=False, is_superuser=False, ):
        if not username:
            raise ValueError('You must set a value for the Username field.')

        user = self.model(username=username, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('The superuser account requires the is_staff attribute to be set to True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('The superuser account requires the is_superuser attribute to be set to True.')

        return self.create_user(username, password, **extra_fields)


class CustomUser(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(
        max_length=120,
        unique=True,
    )

    email = models.EmailField(
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []

    objects= CustomUserHandler()

    def __str__(self):
        return self.username

class Profile(PermissionsMixin, AbstractBaseUser, ):
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        unique=True,
    )
    age = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_length(),

    )
    profileimage = models.URLField(
        blank=True,
        null=False,
    )

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
