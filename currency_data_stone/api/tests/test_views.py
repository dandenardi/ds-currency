from django.test import TestCase, Client
from django.urls import reverse
from api.models import Currency, ExchangeRate

class ExchangeRateViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.usd = Currency.objects.create(code='USD', name='US Dollar')
        self.eur = Currency.objects.create(code='EUR', name='Euro')
        ExchangeRate.objects.create(from_currency=self.usd, to_currency=self.eur, rate=1.2)

    def test_exchange_rate_view(self):
        response = self.client.get(reverse('exchange-rate', args=['USD', 'EUR']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'exchange_rate')

class CurrencyConversionViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.usd = Currency.objects.create(code='USD', name='US Dollar')
        self.eur = Currency.objects.create(code='EUR', name='Euro')
        ExchangeRate.objects.create(from_currency=self.usd, to_currency=self.eur, rate=1.2)
    
    def test_currency_conversion_view(self):
        response = self.client.get(reverse('currency-conversion')+ '?from=USD&to=EUR&amount=100')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'converted_amount')