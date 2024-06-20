# analyze_counter.py
from your_app.models import FinancialData
from datetime import timedelta
from django.utils import timezone

def run():
    # Replace 'ITC.NS' with the actual stock symbol you are interested in
    stock_symbol = 'ITC.NS'

    # Get the current date
    current_date = timezone.now().date()

    # Calculate the date 200 days ago
    start_date = current_date - timedelta(days=200)

    # Retrieve ema20 and closing prices for the specified stock and date range
    data_points = FinancialData.objects.filter(
        symbol=stock_symbol,
        date__range=[start_date, current_date]
    ).order_by('-date').values_list('date', 'ema20', 'close_price')

    # Initialize counter
    counter = 0

    # Iterate through data points from newest to oldest date
    for date, ema20, close_price in data_points:
        if close_price > ema20:
            counter += 1
        elif close_price < ema20:
            counter -= 1

        # Check for a change in behavior
        if counter != 0:
            print(f"For date {date}: Counter value = {counter}")
            break

run()
