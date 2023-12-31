from django.db import models

from LogiSolutions.accounts.models import CustomUser
from LogiSolutions.core.model_mixins import WEIGHT_CHOICES
from LogiSolutions.core.validators import validate_phone_number


class Cargo(models.Model):
    MAX_LENGTH = 200
    NAME_MAX_LENGTH = 100
    CARGO_TYPE_MAX_LENGTH = 100
    CONTACT_NUMBER_MAX_LENGTH = 13
    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )

    location = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH
    )
    cargo_image = models.ImageField(
        null=True,
        blank=True,
        upload_to='cargo_images/'

    )
    contact_number = models.CharField(
        null=False,
        blank=False,
        max_length=CONTACT_NUMBER_MAX_LENGTH,
        default='+359',
        validators=[validate_phone_number]
    )
    is_approved = models.BooleanField(
        default=False
    )

    destination = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LENGTH
    )

    total_km = models.IntegerField(
        null=False,
        blank=False,
    )

    weight = models.CharField(
        max_length=WEIGHT_CHOICES.max_length(),
        choices=WEIGHT_CHOICES.choices(),
    )

    cargo_type = models.CharField(
        max_length=CARGO_TYPE_MAX_LENGTH,
    )

    departure_date = models.DateField(
        null=False,
        blank=False,
    )

    arrival_date = models.DateField(
        null=False,
        blank=False,

    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
