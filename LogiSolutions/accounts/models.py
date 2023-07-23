from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, Permission, Group
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from LogiSolutions.core.model_mixins import Gender, ProfileType


class CustomUserHandler(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given username must be set")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('You must set a value for the Username field.')

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('The superuser account requires the is_staff attribute to be set to True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('The superuser account requires the is_superuser attribute to be set to True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_superuser = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomUserHandler()

    class Meta:
        default_related_name = 'accounts_custom_users'

    def __str__(self):
        return self.email


class Profile(models.Model):
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
        blank=True,
        null=True,
        default=0,
        validators=(
            MaxValueValidator(80),
            MinValueValidator(18),
        )

    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_length(),

    )
    profile_image = models.URLField(
        blank=True,
        null=False,
    )
    type = models.CharField(
        choices=ProfileType.choices(),
        max_length=ProfileType.max_length(),
        default="Cargo Owner",
    )
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
