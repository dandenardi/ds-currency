from django.test import TestCase
from api.models import Currency

class CurrencyModelTest(TestCase):
    def setUp(self):
        Currency.objects.create(code='USD', name='USD Dollar')
        Currency.objects.create(code='EUR', name='Euro')
    
    def test_currency_code(self):
        usd = Currency.objects.get(code='USD')
        eur = Currency.objects.get(code='EUR')
        self.assertEqual(usd.code, 'USD')
        self.assertEqual(eur.code, 'EUR')
    
    def test_currency_name(self):
        usd = Currency.objects.get(code='USD')
        eur = Currency.objects.get(code='EUR')
        self.assertEqual(usd.name, 'USD Dollar')
        self.assertEqual(eur.name, 'Euro') 