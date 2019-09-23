from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import BankInfo
import json
from bankinfo import views as bi_views
from django.contrib.auth.models import User
# Create your tests here.
#token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imtha2FvdGVzdCIsImV4cCI6MTU2OTc4MjQ5NCwiZW1haWwiOiJkaGtpbTcxNUBob3RtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTY5MTc3Njk0fQ.xLQWv0OaXqM9WbJjYVAm5X_Sm4AK4N3EvYoZUKJXOqc'

class simpleTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_csv_read(self):
#        self.client.credentials(HTTP_AUTHORIZATION='JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imtha2FvdGVzdCIsImV4cCI6MTU2OTc4MjQ5NCwiZW1haWwiOiJkaGtpbTcxNUBob3RtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTY5MTc3Njk0fQ.xLQWv0OaXqM9WbJjYVAm5X_Sm4AK4N3EvYoZUKJXOqc')
#        print(client.request)
        response = self.client.get('/api/read/')
#         self.client.login(username='test', password='test')
#         self.client.credentials(HTTP_AUTHORIZATION='JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imtha2FvdGVzdCIsImV4cCI6MTU2OTc4MjQ5NCwiZW1haWwiOiJkaGtpbTcxNUBob3RtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTY5MTc3Njk0fQ.xLQWv0OaXqM9WbJjYVAm5X_Sm4AK4N3EvYoZUKJXOqc')
#        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_device(self):
        response = self.client.get('/api/devices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_allyear(self):
        response = self.client.get('/api/mostallyear/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 #       self.assertEqual(json.loads(response.content)['devices'][0]['device_id'], 'DIS231434')

    def test_inyear(self):
        response = self.client.post('/api/mostinyear/', {'year': '2011'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_indevice(self):
        response = self.client.post('/api/mostindevice/', {'device_id': 'DIS7864654'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)