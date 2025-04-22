import yfinance as yf
import pandas as pd
import taLib
import datetime

# Get the current date
end_date = datetime.datetime.today().strftime('%Y-%m-%d')

# Calculate the start date (2 months ago)
start_date = (datetime.datetime.today() - datetime.timedelta(days=60)).strftime('%Y-%m-%d')

# Download stock data (example: Apple stock) for the last 2 months
data = yf.download("AAPL", start=start_date, end=end_date)

# Display the last few rows of the data with MACD, Signal, and Histogram
print(taLib.getVWAP(data))