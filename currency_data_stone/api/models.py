from django.db import models


from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)

class ExchangeRate(models.Model):
    from_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='from_currency')
    to_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='to_currency')
    rate = models.DecimalField(max_digits=16, decimal_places=6)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.from_currency.code} to {self.to_currency.code}: {self.rate}'