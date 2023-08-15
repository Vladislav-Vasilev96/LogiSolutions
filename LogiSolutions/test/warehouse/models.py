from django.core.exceptions import ValidationError
from django.test import TestCase

from LogiSolutions.accounts.models import CustomUser
from LogiSolutions.warehouse.models import Warehouse

class WarehouseModelTests(TestCase):
    VALID_WAREHOUSE_OWNER = {
        'email': 'testuser@example.com',
        'password': 'testpassword',
    }
    VALID_WAREHOUSE_DATA = {
        'name': 'Test Warehouse',
        'location': 'Test Location',
        'square_meters_capacity': 1000,
        'contact_person': '+359888888888',
    }

    def _create_warehouse(self, data, owner_data=None, **kwargs):
        if owner_data is None:
            owner_data = self.VALID_WAREHOUSE_OWNER

        owner = CustomUser.objects.create_user(**owner_data)
        warehouse_data = {
            **self.VALID_WAREHOUSE_DATA,
            **data,
            **kwargs,
            'owner': owner,
        }
        return Warehouse.objects.create(**warehouse_data)

    def test_warehouseCreate_whenInvalidPhone_shouldRaise(self):
        invalid_data = {
            'contact_person': '0359888888888'
        }

        warehouse = self._create_warehouse(self.VALID_WAREHOUSE_DATA, **invalid_data)

        with self.assertRaises(ValidationError):
            warehouse.full_clean()
            