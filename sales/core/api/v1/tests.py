from core.models import Customer, Order
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class OrderViewSetTestCase(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name='John Doe',
            email='john@example.com',
            phone_number='1234567890',
            city='New York',
            zip_code='10001',
            address='123 Main St'
        )
        self.order1 = Order.objects.create(
            customer=self.customer,
            payment_type=Order.COD,
            status=Order.PENDING,
            product_sku='SKU001',
            quantity=2,
            order_amount=100.00
        )

        self.order2 = Order.objects.create(
            customer=self.customer,
            payment_type=Order.CARD,
            status=Order.CONFIRMED,
            product_sku='SKU002',
            quantity=1,
            order_amount=50.00
        )

    def test_list_orders(self):
        url = reverse('product-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_order(self):
        url = reverse('product-detail', args=[self.order1.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['product_sku'], 'SKU001')
