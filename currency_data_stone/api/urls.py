
from django.urls import path
from .views import CurrencyList, ExchangeRateView, CurrencyConversionView

urlpatterns = [
    
    path('currencies/', CurrencyList.as_view(), name='currency-list'),
    path('exchange-rate/<str:from_currency_code>/<str:to_currency_code>/', ExchangeRateView.as_view(), name='exchange-rate'),
    path('currency-conversion/', CurrencyConversionView.as_view(), name='currency-conversion'),
]
