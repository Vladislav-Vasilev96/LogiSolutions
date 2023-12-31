from django.test import TestCase
from django.urls import reverse
from LogiSolutions.accounts.models import CustomUser
class CreateWarehouseViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='testuser@example.com', password='testpassword')
        self.client.login(email='testuser@example.com', password='testpassword')

    def test_create_warehouse(self):
        form_data = {
            'name': 'Test Warehouse',
            'location': 'Test Location',
            'contact_number': '+359888888888',
            'capacity': 1000,
            'description': 'Test Description',
        }

        url = reverse('create warehouse')
        response = self.client.post(url, data=form_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'warehouse/add-warehouse.html')
