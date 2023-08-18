from django.test import TestCase
from django.urls import reverse

class IndexViewTest(TestCase):
    def test_index_view(self):
        url = reverse('IndexView')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/home.html')


class CargoCatalogViewTest(TestCase):
    def test_cargo_catalog_view(self):
        url = reverse('CargoCatalogView')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/cargo-catalog.html')


class VehicleCatalogViewTest(TestCase):
    def test_vehicle_catalog_view(self):
        url = reverse('VehicleCatalogView')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/vehicle-catalog.html')


class WarehouseCatalogViewTest(TestCase):
    def test_warehouse_catalog_view(self):
        url = reverse('WarehouseCatalogView')  # Replace with your actual URL name
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/warehouse-catalog.html')