from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.models import User, EmailVerification


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.success_data = {
            'username': 'new_user', 'first_name': 'Ivan',
            'last_name': 'Ivanov', 'email': 'ivanivanov@mail.ru',
            'password1': 'zxcvbnmzxc', 'password2': 'zxcvbnmzxc',
        }
        self.fail_data = {
            'username': 'new_user_new', 'first_name': 'Ivan',
            'last_name': 'Ivanov', 'email': 'ivanivanov@mail.ru',
            'password1': 'zxcvbnmzxc', 'password2': 'Zxcvbnmzxc',
        }
        self.path = reverse('users:registration')

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_success_post(self):
        username = self.success_data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.success_data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        confirm_mail = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(confirm_mail.exists())
        self.assertEqual(
            confirm_mail.first().valid_until.date(),
            (now() + timedelta(hours=24)).date()
        )

    def test_user_registration_failed_post(self):
        response = self.client.post(self.path, self.fail_data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'The two password fields didn’t match.')
