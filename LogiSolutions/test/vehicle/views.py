from django.test import TestCase
from django.urls import reverse
from LogiSolutions.accounts.models import CustomUser
from LogiSolutions.vehicle.models import Vehicle
from LogiSolutions.vehicle.forms import VehicleForm

class CreateVehicleViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='testuser@example.com', password='testpassword')
        self.client.login(email='testuser@example.com', password='testpassword')

    def test_create_vehicle(self):
        form_data = {
            'license_plate': 'ABC123',
            'vehicle_type': 'SOME_TYPE',
            'max_weight': '1000',
            'current_location': 'Test Location',
            'contact_number': '+359888888888',
            'is_approved': True,
        }

        url = reverse('create vehicle')
        response = self.client.post(url, data=form_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vehicle/add-vehicle.html')

class EditVehicleViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='testuser@example.com', password='testpassword')
        self.client.login(email='testuser@example.com', password='testpassword')
        self.vehicle = Vehicle.objects.create(license_plate='ABC123', owner=self.user)

    def test_edit_vehicle(self):
        form_data = {
            'license_plate': 'ABC123',
            'vehicle_type': 'SOME_TYPE',
            'max_weight': '1000',
            'current_location': 'Test Location',
            'contact_number': '+359888888888',
            'is_approved': True,
        }


        url = reverse('edit vehicle', kwargs={'pk': self.vehicle.pk})
        response = self.client.post(url, data=form_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vehicle/edit-vehicle.html')
        self.assertEqual(Vehicle.objects.get(pk=self.vehicle.pk).license_plate, 'ABC123')

