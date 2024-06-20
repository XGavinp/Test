import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from Stocks.models import StockData

class Command(BaseCommand):
    help = 'Import stock data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        self.import_stock_data(file_path)

    def import_stock_data(self, file_path):
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Assuming CSV columns are 'Date', 'Open', 'High', 'Low', 'Close', 'Volume'
                date = datetime.strptime(row['Date'], '%Y-%m-%d').date()
                open_price = float(row['Open'])
                high_price = float(row['High'])
                low_price = float(row['Low'])
                close_price = float(row['Close'])
                volume = int(row['Volume'])

                # Create an instance of StockData and save it to the database
                stock_data = StockData(
                    symbol='AAPL',  # You may want to change this or get it from the CSV
                    date=date,
                    open_price=open_price,
                    high_price=high_price,
                    low_price=low_price,
                    close_price=close_price,
                    volume=volume
                )
                stock_data.save()
    # c:\Project\AAPL_past_20_days.csv
