from django.db import models

from LogiSolutions.accounts.models import CustomUser
from LogiSolutions.core.model_mixins import WEIGHT_CHOICES, TypesOfTruck, VehicleStatus, CargoStatus


class Offers(models.Model):
    pass


class Vehicle(models.Model):
    LICENSE_PLATE_MAX_LENGHT = 20
    CURRENT_LOCATION_MAX_LENGHT = 150

    license_plate = models.CharField(
        max_length=LICENSE_PLATE_MAX_LENGHT
    )
    vehicle_type = models.CharField(

        choices=TypesOfTruck.choices(),
        max_length=TypesOfTruck.max_length()
    )
    max_weight = models.CharField(
        max_length=WEIGHT_CHOICES.choices(),
        choices=WEIGHT_CHOICES.choices(),

    )
    current_location = models.CharField(
        max_length=CURRENT_LOCATION_MAX_LENGHT,
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=VehicleStatus.max_length(),
        choices=VehicleStatus.choices(),
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.license_plate


class Cargo(models.Model):
    NAME_MAX_LENGTH = 100

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
        max_length=255
    )

    total_km = models.IntegerField(
        null=False,
        blank=False,
    )

    weight = models.CharField(
        max_length= WEIGHT_CHOICES.max_length(),
        choices=WEIGHT_CHOICES.choices(),
    )

    cargo_type = models.CharField(
        choices=CargoStatus.choices(),
        max_length=CargoStatus.choices(),
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
        max_length=100
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
