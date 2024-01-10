import requests
from decimal import Decimal, getcontext
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Currency, ExchangeRate
from .serializers import CurrencySerializer, ExchangeRateSerializer 


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
            from_currency_code = request.GET.get('from', 'USD')
            to_currency_code = request.GET.get('to', 'BRL')
            amount = Decimal(request.GET.get('amount', 1))

            
            
            getcontext().prec = 28  #
            API_KEY = 'b81190afa89042ba894027d5ae659bfa'
            
            
            url = f'https://exchange-rates.abstractapi.com/v1/live?api_key={API_KEY}&base=USD'

            response = requests.get(url)
            data = response.json()
            

            if 'error' in data:
                return JsonResponse({'error': f'Error obtaining exchange rates: {data["error"]["description"]}'}, status=500)

            
            rates = data['exchange_rates']
            
            from_currency_rate = Decimal(str(rates.get(from_currency_code, 0)))
            
            to_currency_rate = Decimal(str(rates.get(to_currency_code, 0)))

            if from_currency_code == 'USD':
                from_currency_rate = Decimal('1.0')
            if to_currency_code == 'USD':
                to_currency_rate = Decimal('1.0')
            print(from_currency_rate, to_currency_rate)
           
            exchange_rate = to_currency_rate / from_currency_rate
            converted_amount = amount / from_currency_rate * to_currency_rate
            exchange_rate_str = format(exchange_rate, '.10f')
            converted_amount_str = format(converted_amount, '.10f')

            # Calcular o valor convertido
            

            response_data = {
                'from_currency': from_currency_code,
                'to_currency': to_currency_code,
                'exchange_rate': exchange_rate_str,
                'amount': amount,
                'converted_amount': converted_amount_str
        }

            return JsonResponse(response_data)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
class IntroView(View):
    
    template_name = 'intro.html'
    
    def get(self, request):
        
        return render(request, self.template_name)