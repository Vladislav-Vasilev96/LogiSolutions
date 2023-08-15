from django.core.exceptions import ValidationError
from django.test import TestCase
from LogiSolutions.accounts.models import CustomUser
from LogiSolutions.vehicle.models import Vehicle


class VehicleModelTests(TestCase):
    VALID_OWNER_DATA = {
        'email': 'testuser@example.com',
        'password': 'testpassword',
    }
    VALID_VEHICLE_DATA = {
        'license_plate': 'ABC123',
        'vehicle_type': 'SOME_TYPE',
        'max_weight': '1000',
        'current_location': 'Test Location',
        'contact_number': '+359888888888',
        'is_approved': True,
    }

    def _create_vehicle(self, data, owner_data=None, **kwargs):
        if owner_data is None:
            owner_data = self.VALID_OWNER_DATA

        owner = CustomUser.objects.create_user(**owner_data)
        vehicle_data = {
            **self.VALID_VEHICLE_DATA,
            **data,
            **kwargs,
            'owner': owner,
        }
        return Vehicle.objects.create(**vehicle_data)

    def test_vehicleCreate_whenInvalidPhone_shouldRaise(self):
        invalid_data = {
            'contact_number': '0359845546'
        }

        vehicle = self._create_vehicle(self.VALID_VEHICLE_DATA, **invalid_data)

        with self.assertRaises(ValidationError):
            vehicle.full_clean()
