import re

from django.core.exceptions import ValidationError


def validate_phone_number(value):
    pattern = r'^\+359\d{9}$'

    if not re.match(pattern, value):
        raise ValidationError('Invalid mobile phone number')

    if value is None:
        raise ValidationError('Phone cannot be `None`')