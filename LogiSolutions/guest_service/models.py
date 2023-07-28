from django.db import models


class GuestServiceFormSubmission(models.Model):
    PHONE_MAX_LENGTH = 13
    question = models.TextField(
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    phone = models.CharField(
        null=False,
        blank=False,
        max_length=PHONE_MAX_LENGTH,
        default='+359'
    )

    date_asked = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.question
