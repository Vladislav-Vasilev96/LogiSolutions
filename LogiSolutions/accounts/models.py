from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models

from LogiSolutions.core.model_mixins import Gender


class
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
    image = models.URLField(
        blank=True,
        null=False,
    )

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

