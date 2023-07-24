from django.db import models

from LogiSolutions.accounts.models import CustomUser
from LogiSolutions.core.model_mixins import WEIGHT_CHOICES, CargoStatus


class Cargo(models.Model):
    DESTINATION_MAX_LENGTH = 200
    NAME_MAX_LENGTH = 100
    CARGO_TYPE_MAX_LENGTH = 100

    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )

    location = models.CharField(
        null=False,
        blank=False,
    )

    start_location = models.CharField(
        null=False,
        blank=False,
    )

    destination = models.CharField(
        null=False,
        blank=False,
        max_length=DESTINATION_MAX_LENGTH
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

    status = models.CharField(
        choices=CargoStatus.choices(),
        max_length=CargoStatus.max_length(),
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

