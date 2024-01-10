import requests
from .models import ExchangeRate, Currency

def update_exchange_rates():

    '''
        Method used to update the exchange rates. It used initially and API that didn't cover the requirements.
        May be used and adapted for update the values in a more efficient way
    '''
    base_currency_code = 'USD'
    currencies_to_update = ['BRL', 'EUR', 'BTC', 'ETH']

    OPENRATES_APP_ID = '4ad1ab0949534d5397df17bc233f349f'

    for to_currency_code in currencies_to_update:
        if to_currency_code != base_currency_code:
            url = f'https://open.er-api.com/v6/latest/{base_currency_code}?symbols={to_currency_code}&show_alternative=1&apikey={OPENRATES_APP_ID}'
            
            try:
                response = requests.get(url)
                data = response.json()

                if 'error' in data:
                    
                    print(f'Error obtaining the rates from {base_currency_code} to {to_currency_code}: {data["error"]["description"]}')
                else:
                    rate = data['rates'][to_currency_code]

                    from_currency = Currency.objects.get(code=base_currency_code)
                    to_currency = Currency.objects.get(code=to_currency_code)
                    exchange_rate, created = ExchangeRate.objects.get_or_create(
                        from_currency=from_currency,
                        to_currency=to_currency,
                        defaults={'rate': rate}
                    )

                    if not created:
                        exchange_rate.rate = rate
                        exchange_rate.save()

            except requests.RequestException as e:
                print(f'Error obtaining the currency from {base_currency_code} to {to_currency_code}: {e}')
            

