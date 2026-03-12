from fastapi import FastAPI
import yfinance as yf
import pandas as pd
from ai_analysis import analyze_stock

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Saham Dashboard"}

@app.get("/stock/{symbol}")
def get_stock(symbol: str):
    data = yf.download(symbol, period="3mo")
    return data.tail().to_dict()

@app.get("/analysis/{symbol}")
def ai_analysis(symbol: str):
    result = analyze_stock(symbol)
    return result
