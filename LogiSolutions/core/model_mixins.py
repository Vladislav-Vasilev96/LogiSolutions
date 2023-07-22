from enum import Enum


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class ChoicesStringsMixin:

    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls)


class Gender(ChoicesStringsMixin, ChoicesMixin, Enum):
    MALE = 'male'
    FEMALE = 'female'
    DO_NOT_SHOW = 'do not show'


class VehicleStatus(ChoicesStringsMixin, ChoicesMixin, Enum):
    DELIVERED = 'delivered'
    AWAITING_DELIVERY = 'waiting for delivery'
    WAITING_FOR_LOAD = 'waiting for load'
    ON_BREAK = 'on a break'
    IN_PROCESS = 'in process'


class CargoStatus(ChoicesStringsMixin, ChoicesMixin, Enum):
    PENDING = 'Pending'
    IN_TRANSIT = 'In Transit'
    DELIVERED = 'Delivered'
    TO_STORAGE = 'To storage '
    LOST = 'Lost'
    CANCELLED = 'Cancelled'


class WEIGHT_CHOICES(ChoicesStringsMixin, ChoicesMixin, Enum):
    B = '1.4'
    C = '10'
    CE = '24'


class TypesOfTruck(ChoicesStringsMixin, ChoicesMixin, Enum):
    TANK_TRUCK = 'Tank truck'
    FLATBED_TRUCK = 'Flatbed truck'
    REFRIGERATOR_TRUCK = 'Refrigerator truck'
    LIGHT_TRUCK = 'Light truck'
    CAR_CARRIER_TRAILER = 'Car Carrier Trailer'
    GARBAGE_TRUCK = 'Garbage truck'
    MAIL_TRUCK = 'Mail truck'


class PaymentsStatus(ChoicesStringsMixin, ChoicesMixin, Enum):
    PAID = 'Paid'
    PENDING = 'Pending'
    OVERDUE = 'Overdue'



class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        fields = [(str_field, getattr(self, str_field, None)) for str_field in self.str_fields]
        return ', '.join(f' {name}={value}' for (name, value) in fields)
