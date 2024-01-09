from decimal import Decimal
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View
from django.http import JsonResponse
from .models import Currency, ExchangeRate
from .serializers import CurrencySerializer, ExchangeRateSerializer
from api.utils import update_exchange_rates


class CurrencyList(APIView):
    def get(self, request):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)

class ExchangeRateView(APIView):
    def get(self, request, from_currency_code, to_currency_code):
        from_currency = Currency.objects.get(code=from_currency_code)
        to_currency = Currency.objects.get(code=to_currency_code)

        exchange_rate = ExchangeRate.objects.get(from_currency=from_currency, to_currency=to_currency)
        serializer = ExchangeRateSerializer(exchange_rate)
        return Response({'exchange_rate': serializer.data['rate']})


class CurrencyConversionView(View):
    def get(self, request):
        try:
            from_currency_code = request.GET.get('from')
            to_currency_code = request.GET.get('to')
            amount = Decimal(request.GET.get('amount', 1))

            from_currency = Currency.objects.get(code=from_currency_code)
            to_currency = Currency.objects.get(code=to_currency_code)

            exchange_rate = ExchangeRate.objects.filter(from_currency=from_currency, to_currency = to_currency).latest('last_updated')

            converted_amount = amount * exchange_rate.rate

            response_data = {
                'from_currency': from_currency.code,
                'to_currency': to_currency.code,
                'exchange_rate': exchange_rate.rate,
                'amount': amount,
                'converted_amount': converted_amount
            }

            return JsonResponse(response_data)
        
        except Currency.DoesNotExist:
            return JsonResponse({'error': 'Currency not found'}, status=404)
        except ExchangeRate.DoesNotExist:
            return JsonResponse({'error': 'Exchange rate not found'}, status=404)