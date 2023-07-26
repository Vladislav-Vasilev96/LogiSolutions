from django.db import models

from LogiSolutions.accounts.models import CustomUser
from LogiSolutions.core.model_mixins import TypesOfTruck, WEIGHT_CHOICES, VehicleStatus


class Vehicle(models.Model):
    LICENSE_PLATE_MAX_LENGHT = 20
    CURRENT_LOCATION_MAX_LENGHT = 150
    CONTACT_NUMBER_MAX_LENGTH=12

    license_plate = models.CharField(
        max_length=LICENSE_PLATE_MAX_LENGHT
    )
    vehicle_type = models.CharField(

        choices=TypesOfTruck.choices(),
        max_length=TypesOfTruck.max_length()
    )
    max_weight = models.CharField(
        max_length=WEIGHT_CHOICES.max_length(),
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
    vehicle_image= models.ImageField(
        null=True,
        blank=True,
        upload_to='vehicle_images'

    )
    contact_number = models.CharField(
        null=False,
        blank=False,
        max_length=CONTACT_NUMBER_MAX_LENGTH,
        default='359'
    )

    owner = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    def __str__(self):
        return self.license_plate
