from enum import Enum


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.value, choice.value) for choice in cls]


class ChoicesStringsMixin:

    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls)


class Gender(ChoicesStringsMixin, ChoicesMixin, Enum):
    MALE = 'male'
    FEMALE = 'female'
    DO_NOT_SHOW = 'do not show'


class WEIGHT_CHOICES(ChoicesStringsMixin, ChoicesMixin, Enum):
    B = 'Up to 1.4 tons'
    C = 'Up to 10 tons'
    CE = 'Up to 24 tons'


class TypesOfTruck(ChoicesStringsMixin, ChoicesMixin, Enum):
    TANK_TRUCK = 'Tank truck'
    FLATBED_TRUCK = 'Flatbed truck'
    REFRIGERATOR_TRUCK = 'Refrigerator truck'
    LIGHT_TRUCK = 'Light truck'
    CAR_CARRIER_TRAILER = 'Car Carrier Trailer'
    GARBAGE_TRUCK = 'Garbage truck'
    MAIL_TRUCK = 'Mail truck'


class ProfileType(ChoicesStringsMixin, ChoicesMixin, Enum):
    Vehicle_OWNER = 'Vehicle Owner'
    CARGO_OWNER = 'Cargo Owner'
    WAREHOUSE = 'Warehouse Owner'


class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        fields = [(str_field, getattr(self, str_field, None)) for str_field in self.str_fields]
        return ', '.join(f' {name}={value}' for (name, value) in fields)
