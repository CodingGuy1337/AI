import pandas as pd
def getMACD(data, x, y, z):
    # Step 1: Calculate 12-period EMA
    data['EMA12'] = data['Close'].ewm(span=x, adjust=False).mean()

    # Step 2: Calculate 26-period EMA
    data['EMA26'] = data['Close'].ewm(span=y, adjust=False).mean()

    # Step 3: Calculate MACD line (12-EMA - 26-EMA)
    data['MACD'] = data['EMA12'] - data['EMA26']

    # Step 4: Calculate Signal line (9-period EMA of MACD)
    data['Signal'] = data['MACD'].ewm(span=z, adjust=False).mean()

    # Step 5: Calculate Histogram (MACD - Signal line)
    data['Histogram'] = data['MACD'] - data['Signal']

    return data[['Close', 'MACD', 'Signal', 'Histogram']]

def getEMA(data, period):
    # Calculate the Exponential Moving Average (EMA)
    data['EMA'] = data['Close'].ewm(span=period, adjust=False).mean()
    return data[['Close', 'EMA']]

def getSMA(data, period):
    # Calculate the Simple Moving Average (SMA)
    data['SMA'] = data['Close'].rolling(window=period).mean()
    return data[['Close', 'SMA']]

def getRSI(data, period):
    # Calculate the Relative Strength Index (RSI)
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data[['Close', 'RSI']]

def getBollingerBands(data, period, num_std_dev):
    # Calculate the Simple Moving Average (SMA)
    data['SMA'] = data['Close'].rolling(window=period).mean()

    # Calculate the rolling standard deviation
    data['Rolling Std'] = data['Close'].rolling(window=period).std()

    # Calculate the Upper and Lower Bollinger Bands
    data['Upper Band'] = data['SMA'] + (data['Rolling Std'] * num_std_dev)
    data['Lower Band'] = data['SMA'] - (data['Rolling Std'] * num_std_dev)

    return data[['Close', 'SMA', 'Upper Band', 'Lower Band']]


def getStochasticOscillator(data, k_period=14, d_period=3):
    # Make sure 'High' and 'Low' exist
    if 'High' not in data.columns or 'Low' not in data.columns:
        raise ValueError("Data must contain 'High' and 'Low' columns")

    # Calculate L14 (lowest low) and H14 (highest high) over the k-period window
    L14 = data['Low'].rolling(window=k_period).min()
    H14 = data['High'].rolling(window=k_period).max()

    # Avoid division by zero
    denominator = (H14 - L14).replace(0, 1e-10)

    # Calculate %K and %D
    data['%K'] = 100 * ((data['Close'] - L14) / denominator)
    data['%D'] = data['%K'].rolling(window=d_period).mean()

    return data[['Close', '%K', '%D']]

def getMomentum(data, period):
    # Calculate the Momentum
    data['Momentum'] = data['Close'].diff(periods=period)
    return data[['Close', 'Momentum']]

def getATR(data, period):
    # Calculate True Range (TR)
    data['High-Low'] = data['High'] - data['Low']
    data['High-Prev Close'] = abs(data['High'] - data['Close'].shift(1))
    data['Low-Prev Close'] = abs(data['Low'] - data['Close'].shift(1))
    data['TR'] = data[['High-Low', 'High-Prev Close', 'Low-Prev Close']].max(axis=1)

    # Calculate Average True Range (ATR)
    data['ATR'] = data['TR'].rolling(window=period).mean()

    return data[['Close', 'ATR']]

def getVolume(data, period):
    # Calculate the Volume Moving Average
    data['Volume MA'] = data['Volume'].rolling(window=period).mean()
    return data[['Close', 'Volume', 'Volume MA']]

def getVWAP(data):
    # Calculate the VWAP
    data['Cumulative Volume'] = data['Volume'].cumsum()
    data['Cumulative Price Volume'] = (data['Close'] * data['Volume']).cumsum()
    data['VWAP'] = data['Cumulative Price Volume'] / data['Cumulative Volume']
    return data[['Close', 'VWAP']]


    
