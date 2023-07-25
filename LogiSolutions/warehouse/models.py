from django.db import models

from LogiSolutions.accounts.models import CustomUser


class Warehouse(models.Model):
    NAME_MAX_LENGTH = 100
    LOCATION_MAX_LENGTH = 200
    CONTACT_PERSON_MAX_LENGTH = 100

    name = models.CharField(
        max_length=NAME_MAX_LENGTH

    )
    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH
    )
    square_meters_capacity = models.PositiveIntegerField(

    )

    contact_person = models.CharField(
        max_length=CONTACT_PERSON_MAX_LENGTH
    )

    owner = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.name