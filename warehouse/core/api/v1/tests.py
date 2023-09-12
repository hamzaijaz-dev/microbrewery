from core.models import Product, Warehouse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class ProductViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.warehouse = Warehouse.objects.create(name='My store', location='Lahore, Pakistan')
        self.product_data = {
            "name": "Test Product",
            "sku": "SKU1",
            "description": "A test product",
            "price": "10.99",
            "warehouse": self.warehouse
        }
        self.product = Product.objects.create(**self.product_data)
        self.url = 'http://localhost:8001/api/v1/warehouse/products/'

    def test_list_products(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_product(self):
        response = self.client.get(f'{self.url}{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)
