from django.test import TestCase, Client
import unittest



# Create your tests here.


class AccountsTest(unittest.TestCase):
    def test_home(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_auth(self):
        client = Client()
        response = client.post('/login', {'username': 'josh', 'password': 'rutawanya'})
        self.assertEqual(response.status_code, 200)
