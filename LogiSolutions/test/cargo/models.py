from django.core.exceptions import ValidationError
from django.test import TestCase

from LogiSolutions.accounts.models import CustomUser
from LogiSolutions.cargo.models import Cargo


class CargoModelTests(TestCase):
    VALID_CARGO_OWNER = {
        'email': 'testuser@example.com',
        'password': 'testpassword',
    }
    VALID_CARGO_DATA = {
        'name': 'Test Cargo',
        'location': 'Test Location',
        'contact_number': '+359888888888',
        'destination': 'Test Destination',
        'total_km': 150,
        'weight': '1000',
        'cargo_type': 'Test Type',
        'departure_date': '2023-08-06',
        'arrival_date': '2023-08-08',
        'description': 'Test Description',
    }

    def _create_cargo(self, data, owner_data=None, **kwargs):
        if owner_data is None:
            owner_data = self.VALID_CARGO_OWNER

        owner = CustomUser.objects.create_user(**owner_data)
        cargo_data = {
            **self.VALID_CARGO_DATA,
            **data,
            **kwargs,
            'owner': owner,
        }
        return Cargo.objects.create(**cargo_data)

    def test_cargoCreate_whenInvalidPhone_shouldRaise(self):
        invalid_data = {
            'contact_number': '0359888888888'
        }

        cargo = self._create_cargo(self.VALID_CARGO_DATA, **invalid_data)

        with self.assertRaises(ValidationError):
            cargo.full_clean()
