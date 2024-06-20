import csv

from .models import Sectors, Stocks

def import_data(csv_file_path):
  """
  Imports data from a CSV file into Sectors and Stocks models.

  Args:
      csv_file_path (str): Path to the CSV file containing the data.
  """
  with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
      # Create a Sector object (if it doesn't exist)
      sector, created = Sectors.objects.get_or_create(symbol=row['symbol'])
      sector.name = row['name']
      sector.isincode = row['isincode'] if 'isincode' in row else ''  # Handle optional field
      sector.save()

      # Create a Stock object
      stock = Stocks.objects.create(
          name=row['name'],
          symbol=row['symbol'],
          isincode=row['isincode'] if 'isincode' in row else '',  # Handle optional field
      )

      # Add stock to the sector (if ManyToMany relationship field name is different)
      if 'sectors' in row:  # Adjust if the field name is different in your model
        sector.stocks.add(stock)
      sector.save()

# Example usage (replace 'data.csv' with your actual file path)
import_data('C:/Users/ojhaa/Desktop/Test MP/StockTracker/data.csv')
