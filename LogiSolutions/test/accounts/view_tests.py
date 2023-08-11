from django.test import TestCase, Client
from django.urls import reverse

from LogiSolutions.accounts.models import CustomUser


class RegisterUserViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_user(self):
        form_data = {
            'email': 'user@example.com',
            'password1': 'password',
            'password2': 'password',
        }

        url = reverse('RegisterView')

        response = self.client.post(url, data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_register_existing_user(self):
        existing_email = 'vladisslav.vasilev9601@gmail.com'
        CustomUser.objects.create(email=existing_email)

        form_data = {
            'email': existing_email,
            'password1': 'samolet2',
            'password2': 'samolet2',
        }
        url = reverse('RegisterView')
        response = self.client.post(url, data=form_data)

        existing_user = CustomUser.objects.filter(email=existing_email)
        self.assertTrue(existing_user.exists())

        self.assertEqual(response.status_code, 200)
    def test_register_invalid_passwords(self):

        form_data = {
            'email': 'testuser@example.com',
            'password1': 'testpassword1',
            'password2': 'testpassword2',
        }
        url = reverse('RegisterView')
        response = self.client.post(url, data=form_data)

        self.assertEqual(response.status_code, 400)

    # def test_register_no_password(self):
    #     form_data = {
    #         'email': 'testuser@example.com',
    #         'password1': '',
    #         'password2': '',
    #     }
    #     url = reverse('RegisterView')
    #     response = self.client.post(url, data=form_data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'This field is required', status_code=400)
    #
    #
