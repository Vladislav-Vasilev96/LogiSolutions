from django.db import models

# Create your models here.
# class Vehicle(models.Model):
#     LICENSE_PLATE_MAX_LENGHT = 20
#     CURRENT_LOCATION_MAX_LENGHT = 150
#
#     license_plate = models.CharField(
#         max_length=LICENSE_PLATE_MAX_LENGHT
#     )
#     vehicle_type = models.CharField(
#
#         choices=TypesOfTruck.choices(),
#         max_length=TypesOfTruck.max_length()
#     )
#     max_weight = models.CharField(
#         max_length=WEIGHT_CHOICES.choices(),
#         choices=WEIGHT_CHOICES.choices(),
#
#     )
#     current_location = models.CharField(
#         max_length=CURRENT_LOCATION_MAX_LENGHT,
#         null=True,
#         blank=True,
#     )
#
#     status = models.CharField(
#         max_length=VehicleStatus.max_length(),
#         choices=VehicleStatus.choices(),
#     )
#
#     description = models.TextField(
#         null=True,
#         blank=True,
#     )
#
#     owner = models.ForeignKey(
#         CustomUser,
#         on_delete=models.CASCADE
#     )
#
#     def __str__(self):
#         return self.license_plate
#