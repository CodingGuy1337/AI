import pandas as pd

def getMACD(data, x, y, z):
    data['EMA12'] = data['Close'].ewm(span=x, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=y, adjust=False).mean()
    data['MACD'] = data['EMA12'] - data['EMA26']
    data['Signal'] = data['MACD'].ewm(span=z, adjust=False).mean()
    data['Histogram'] = data['MACD'] - data['Signal']
    return data[['MACD', 'Signal', 'Histogram']]

def getEMA(data, period):
    data['EMA'] = data['Close'].ewm(span=period, adjust=False).mean()
    return data[['EMA']]

def getSMA(data, period):
    data['SMA'] = data['Close'].rolling(window=period).mean()
    return data[['SMA']]

def getRSI(data, period):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data[['RSI']]

def getBollingerBands(data, period, num_std_dev):
    data['SMA'] = data['Close'].rolling(window=period).mean()
    data['Rolling Std'] = data['Close'].rolling(window=period).std()
    data['Upper Band'] = data['SMA'] + (data['Rolling Std'] * num_std_dev)
    data['Lower Band'] = data['SMA'] - (data['Rolling Std'] * num_std_dev)
    return data[['SMA', 'Upper Band', 'Lower Band']]

def getStochasticOscillator(data, k_period=14, d_period=3):
    if 'High' not in data.columns or 'Low' not in data.columns:
        raise ValueError("Data must contain 'High' and 'Low' columns")
    L14 = data['Low'].rolling(window=k_period).min()
    H14 = data['High'].rolling(window=k_period).max()
    denominator = (H14 - L14).replace(0, 1e-10)
    data['%K'] = 100 * ((data['Close'] - L14) / denominator)
    data['%D'] = data['%K'].rolling(window=d_period).mean()
    return data[['%K', '%D']]

def getMomentum(data, period):
    data['Momentum'] = data['Close'].diff(periods=period)
    return data[['Momentum']]

def getATR(data, period):
    data['High-Low'] = data['High'] - data['Low']
    data['High-Prev Close'] = abs(data['High'] - data['Close'].shift(1))
    data['Low-Prev Close'] = abs(data['Low'] - data['Close'].shift(1))
    data['TR'] = data[['High-Low', 'High-Prev Close', 'Low-Prev Close']].max(axis=1)
    data['ATR'] = data['TR'].rolling(window=period).mean()
    return data[['ATR']]

def getVolume(data, period):
    data['Volume MA'] = data['Volume'].rolling(window=period).mean()
    return data[['Volume MA']]

def getVWAP(data):
    data['Cumulative Volume'] = data['Volume'].cumsum()
    data['Cumulative Price Volume'] = (data['Close'] * data['Volume']).cumsum()
    data['VWAP'] = data['Cumulative Price Volume'] / data['Cumulative Volume']
    return data[['VWAP']]
