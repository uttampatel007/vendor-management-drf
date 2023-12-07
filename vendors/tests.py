from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from .models import Vendor, PurchaseOrder


class VendorCreateListAPITests(TestCase):
    def setUp(self):
        # Initialize test data
        self.client = APIClient()
        self.url = reverse('vendors:vendors')

        self.valid_payload = {
                "name": "Vendor 2",
                "contact_details": "8200088393",
                "address": "Bhuj Kutch",
                "vendor_code": "vendor2",
                "on_time_delivery_rate": 0,
                "quality_rating_avg": 0,
                "average_response_time": 0,
                "fulfillment_rate": 0
        }
        
        # Create a token for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


    def test_get_all_objects(self):
        # Test GET request for retrieving all objects
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_object(self):
        # Test POST request for creating an object
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class VendorDetailUpdateDeleteAPITests(TestCase):
    def setUp(self):
        # Initialize test data
        self.client = APIClient()

        self.valid_payload = {
                "name": "Vendor 2",
                "contact_details": "8200088393",
                "address": "Bhuj Kutch",
                "vendor_code": "vendor2",
                "on_time_delivery_rate": 0,
                "quality_rating_avg": 0,
                "average_response_time": 0,
                "fulfillment_rate": 0
        }
        self.test_object = Vendor.objects.create(**self.valid_payload)
        
        self.url = reverse('vendors:vendor-detail', args=[self.test_object.pk])

        # Create a token for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_single_object(self):
        # Test GET request for retrieving a single object
        response = response = self.client.get(self.url, pk=self.test_object.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
