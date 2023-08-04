from django import test
from django.urls import reverse


class CreateTestDataMixin(test.TestCase):
    valid_register_user_data = {
        'email': 'testov@test.com',
        'password1': 'strong_password_1234',
        'password2': 'strong_password_1234',
    }

    valid_login_user_data = {
        'email': 'testov@test.com',
        'password': 'unbreakable_password_1234',
    }

