from django.db import models

from LogiSolutions.core.model_mixins import STATUS_CHOICES


# Create your models here.
class Offers(models.Model):
    pass


class Vehicle(models.Model):
    license_plate = models.CharField(
        max_length=20
    )
    vehicle_type = models.CharField(
        max_length=100
    )
    capacity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    current_location = models.CharField(
        max_length=255
    )

    model = models.CharField(
        max_length=100
    )
    year = models.PositiveIntegerField(

    )
    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='ready',
    )

    def __str__(self):
        return self.license_plate


class Cargo(models.Model):
    name = models.CharField(
        max_length=255
    )

    location = models.CharField(

    )

    start_location = models.CharField(

    )

    destination = models.CharField(
        max_length=255
    )

    weight = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.IntegerField(

    )

    cargo_type = models.CharField(
        max_length=100
    )

    departure_date = models.DateField(

    )

    arrival_date = models.DateField(

    )

    status = models.CharField(
        max_length=100
    )
#     owner = models.ForeignKey(
#     'auth.User',
#     on_delete=models.CASCADE
#     )
