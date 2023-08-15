from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

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
    def test_register_without_email(self):

        form_data = {
            'email': '',
            'password1': 'testpassword1',
            'password2': 'testpassword1',
        }
        url = reverse('RegisterView')
        response = self.client.post(url, data=form_data)

        self.assertEqual(response.status_code, 200)

        expected_error_message = "This field is required."
        self.assertContains(response, expected_error_message)


    def test_register_with_too_common_password_and_entirely_numeric(self):
        form_data = {
            'email': 'test@abv.bg',
            'password1': '123456789',
            'password2': '123456789',
        }
        url = reverse('RegisterView')
        response = self.client.post(url, data=form_data)

        self.assertEqual(response.status_code, 200)

        expected_error_message = "This password is too common."
        self.assertContains(response, expected_error_message)

        expected_error_message2= "This password is entirely numeric."
        self.assertContains(response, expected_error_message2)

    def test_register_with_too_short_password(self):
        form_data = {
            'email': 'test@abv.bg',
            'password1': 'mypass',
            'password2': 'mypass',
        }
        url = reverse('RegisterView')
        response = self.client.post(url, data=form_data)

        self.assertEqual(response.status_code, 200)

        expected_error_message = "This password is too short. It must contain at least 8 characters."
        self.assertContains(response, expected_error_message)

    def test_register_with_wrong_second_password(self):
        form_data = {
            'email': 'test@abv.bg',
            'password1': 'mypassword2',
            'password2': 'mypassword1',
        }
        url = reverse('RegisterView')
        response = self.client.post(url, data=form_data)

        self.assertEqual(response.status_code, 200)

        expected_error_message = "The two password fields didn't match."
        self.assertContains(response, expected_error_message)

