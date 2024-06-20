# Inside yourapp/management/commands/calculate_ema_counts.py
from django.core.management.base import BaseCommand
from Stocks.views import calculate_ema_counts_for_all_stocks

class Command(BaseCommand):
    help = 'Calculate EMA counts for all stocks'

    def handle(self, *args, **options):
        calculate_ema_counts_for_all_stocks()
        self.stdout.write(self.style.SUCCESS('Successfully calculated EMA counts'))
