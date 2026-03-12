import yfinance as yf
import pandas as pd

def analyze_stock(symbol):

    data = yf.download(symbol, period="6mo")

    data['MA20'] = data['Close'].rolling(20).mean()
    data['MA50'] = data['Close'].rolling(50).mean()

    last = data.iloc[-1]

    if last['MA20'] > last['MA50']:
        trend = "Bullish"
    else:
        trend = "Bearish"

    return {
        "symbol": symbol,
        "price": float(last['Close']),
        "trend": trend,
        "MA20": float(last['MA20']),
        "MA50": float(last['MA50'])
    }
