from core.models import Revenue
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class RevenueViewSetTestCase(APITestCase):
    def setUp(self):
        self.revenue1 = Revenue.objects.create(
            reference_number='ORDER001',
            revenue_amount=1000.00
        )

        self.revenue2 = Revenue.objects.create(
            reference_number='ORDER002',
            revenue_amount=1500.50
        )

    def test_list_revenues(self):
        url = reverse('revenue_details-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
