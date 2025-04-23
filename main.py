import yfinance as yf
import pandas as pd
from taLib import (
    getMACD,
    getEMA,
    getSMA,
    getRSI,
    getBollingerBands,
    getStochasticOscillator,
    getMomentum,
    getATR,
    getVolume,
    getVWAP,
)
import datetime

# Main script
# Get the current date
end_date = datetime.datetime.today().strftime('%Y-%m-%d')

# Calculate the start date (2 months ago)
start_date = (datetime.datetime.today() - datetime.timedelta(days=59)).strftime('%Y-%m-%d')

# Download stock data (example: Apple stock) for the last 2 months
data = yf.download("AAPL", start=start_date, end=end_date, interval="5m")

# Calculate indicators
macd_data = getMACD(data, 12, 26, 9)
ema_data = getEMA(data, 20)
sma_data = getSMA(data, 50)
rsi_data = getRSI(data, 14)
bollinger_bands = getBollingerBands(data, 20, 2)
stochastic_oscillator = getStochasticOscillator(data)
momentum_data = getMomentum(data, 10)
atr_data = getATR(data, 14)
volume_data = getVolume(data, 20)
vwap_data = getVWAP(data)

# Combine all indicators into a single table
data_table = pd.concat([data, macd_data, ema_data, sma_data, rsi_data,
                        bollinger_bands, stochastic_oscillator, momentum_data,
                        atr_data, volume_data, vwap_data], axis=1)

# Display the last few rows of the data table
print(data_table)