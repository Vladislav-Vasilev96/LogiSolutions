from django.test import TestCase
from django.urls import reverse
from LogiSolutions.accounts.models import CustomUser
from LogiSolutions.cargo.models import Cargo


class CreateCargoViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='testuser@example.com', password='testpassword')
        self.client.login(email='testuser@example.com', password='testpassword')

    def test_create_cargo(self):
        form_data = {
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

        url = reverse('create cargo')
        response = self.client.post(url, data=form_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cargo/add-cargo.html')


