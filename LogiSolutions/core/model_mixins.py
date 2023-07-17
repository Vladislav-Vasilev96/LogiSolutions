from enum import Enum


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class ChoicesStringsMixin:

    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls)

class Gender(ChoicesStringsMixin,ChoicesMixin, Enum):
    MALE = 'male'
    FEMALE = 'female'
    DO_NOT_SHOW = 'do not show'

class Status(ChoicesStringsMixin,ChoicesMixin, Enum):
    DELIVERED = 'delivered'
    AWAITING_DELIVERY = 'waiting for  delivery'
    WAITING_FOR_LOAD = 'waiting for load'
    ON_BREAK = 'on a break'
    IN_PROCESS = 'in process'


STATUS_CHOICES = [
        ('available', 'Available'),
        ('on_way', 'On the Way'),
    ]
class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        fields = [(str_field, getattr(self, str_field, None)) for str_field in self.str_fields]
        return ', '.join(f' {name}={value}' for (name, value) in fields)
