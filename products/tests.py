from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product, Tariff, Promotion


class ProductTariffViewTests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product')
        self.tariff = Tariff.objects.create(name='Test Tariff', price=100.00, product=self.product)
        self.promotion = Promotion.objects.create(
            name='Test Promotion',
            discount_percentage=20.00,
            start_date='2024-01-01',
            end_date='2024-12-31'
        )
        self.promotion.tariffs.add(self.tariff)
        self.url = reverse('product-tariffs')

    def test_product_tariff_view(self):
        response = self.client.get(self.url, HTTP_ACCEPT='application/xml')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, '<name>Test Product</name>')
        self.assertContains(response, '<name>Test Tariff</name>')
        self.assertContains(response, '<name>Test Promotion</name>')
        self.assertContains(response, '<discount_percentage>20.00</discount_percentage>')



