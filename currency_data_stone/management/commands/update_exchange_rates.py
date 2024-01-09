from django.core.management.base import BaseCommand
from api.utils import update_exchange_rates

class Command(BaseCommand):
    help = 'Updates the exchange rates'

    def handle(self, *args, **options):
        update_exchange_rates()
        self.stdout.write(self.style.SUCCESS('Exchange rates updated!'))