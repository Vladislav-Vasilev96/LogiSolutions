from django.db import models


class GuestServiceFormSubmission(models.Model):
    question = models.TextField(
        blank=True,
        null=True
    )
    email = models.EmailField(

    )
    phone = models.CharField(
        max_length=20)

    def __str__(self):
        return self.question
