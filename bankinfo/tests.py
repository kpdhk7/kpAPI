from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from rest_framework import status
from .models import BankInfo
from django.contrib.auth.models import User
# Create your tests here.
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imtha2FvdGVzdCIsImV4cCI6MTU2OTc4MjQ5NCwiZW1haWwiOiJkaGtpbTcxNUBob3RtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTY5MTc3Njk0fQ.xLQWv0OaXqM9WbJjYVAm5X_Sm4AK4N3EvYoZUKJXOqc'

class simpleTest(APITestCase):
    def test_csv_read(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imtha2FvdGVzdCIsImV4cCI6MTU2OTc4MjQ5NCwiZW1haWwiOiJkaGtpbTcxNUBob3RtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTY5MTc3Njk0fQ.xLQWv0OaXqM9WbJjYVAm5X_Sm4AK4N3EvYoZUKJXOqc')
        print(client.request)
        response = client.get('/api/read/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
