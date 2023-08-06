from django.db import models

from LogiSolutions.accounts.models import CustomUser
from LogiSolutions.core.validators import validate_phone_number


class Warehouse(models.Model):
    NAME_MAX_LENGTH = 100
    LOCATION_MAX_LENGTH = 200
    CONTACT_PERSON_MAX_LENGTH = 13

    name = models.CharField(
        max_length=NAME_MAX_LENGTH

    )
    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH
    )
    square_meters_capacity = models.PositiveIntegerField(

    )

    contact_person = models.CharField(
        max_length=CONTACT_PERSON_MAX_LENGTH,
        null=False,
        blank=False,
        default='+359',
        validators=[validate_phone_number]

    )
    warehouse_image = models.ImageField(
        null=True,
        blank=True,
        upload_to='warehouse_images/'

    )
    is_approved = models.BooleanField(
        default=False
    )

    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )



    def __str__(self):
        return self.name
