
from django.test import TestCase
from .models import ServiceForm, Articles
from django.contrib.auth import get_user_model
from django.test import Client
# Python
from http import HTTPStatus
# Models
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    # Проверка  загрузки страницы входа и регистрации
    def test_is_ok_page_login(self):
        response = self.c.get('/login/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_is_ok_page_register(self):
        response = self.c.get('/register/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # Проверка логирования и входа в кабинет
    def test_login_user(self):
        credentials = {
            'username': 'Ivan Login',
            'password': '4efefwefefwefB3rgVM'
        }

        user = User.objects.create_user(**credentials)
        response = self.c.post('/login/', credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)

    # # Проверка регистрации
    # def test_register_user(self):
    #
    #     data = {
    #         'username': 'TestIvan',
    #         'email': 'ivan@mail.com',
    #         'password': '4ABefef3rgVM',
    #         'password_confirmation': '4ABefef3rgVM',
    #     }
    #
    #     response = self.c.post('/register/', data)
    #
    #     try:
    #         user = User.objects.get(username=data['username'])
    #     except User.DoesNotExist:
    #         user = NULL
    #
    #     self.assertIsInstance(user, User)