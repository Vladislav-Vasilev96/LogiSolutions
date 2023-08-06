import re

from django.core.exceptions import ValidationError


def validate_phone_number(value):
    pattern = r'^\+359\d{9}$'

    if not re.Match(pattern, value):
        raise ValidationError('Invalid mobile phone number.')