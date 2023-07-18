from django.db import models

from LogiSolutions.core.model_mixins import STATUS_CHOICES, WEIGHT_CHOICES, TypesOfTruck


class Offers(models.Model):
    pass


class Vehicle(models.Model):
    LICENSE_PLATE_MAX_LENGHT = 20
    VEHICLE_TYPE_MAX_LENGHT = 100
    CURRENT_LOCATION_MAX_LENGHT = 150
    license_plate = models.CharField(
        max_length=LICENSE_PLATE_MAX_LENGHT
    )
    vehicle_type = models.CharField(

        choices=TypesOfTruck.choices(),
        max_length=TypesOfTruck.max_length()
    )
    max_weight = models.DecimalField(
        choices=WEIGHT_CHOICES.choices(),
        max_digits=10,
        decimal_places=2
    )
    current_location = models.CharField(
        max_length=CURRENT_LOCATION_MAX_LENGHT,
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='ready',
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.license_plate


class Cargo(models.Model):
    name = models.CharField(
        max_length=255
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

    weight = models.DecimalField(
        choices=WEIGHT_CHOICES.choices(),
        max_digits=10,
        decimal_places=2
    )

    cargo_type = models.CharField(
        max_length=100
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
#     owner = models.ForeignKey(
#     'auth.User',
#     on_delete=models.CASCADE
#     )
