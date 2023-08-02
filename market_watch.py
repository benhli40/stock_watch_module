import os
import json
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

def read_api_key_from_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data['api_key']

def get_realtime_stock_prices(api_key, symbol):
    ts = TimeSeries(key=api_key, output_format='json')
    data, meta_data = ts.get_quote_endpoint(symbol=symbol)
    if '05. price' in data:
        return data['05. price']
    else:
        return None

def get_sma_for_symbol(api_key, symbol):
    ti = TechIndicators(key=api_key, output_format='json')
    data, meta_data = ti.get_sma(symbol=symbol)
    if 'SMA' in data and len(data['SMA']) > 0:
        return data['SMA'][0]['SMA']
    else:
        return None

if __name__ == '__main__':
    api_key_file_path = 'api_key.json'
    api_key = read_api_key_from_file(api_key_file_path)

    stock_symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']  # Add more symbols if needed

    print("Real-time stock prices:")
    for symbol in stock_symbols:
        stock_price = get_realtime_stock_prices(api_key, symbol)
        if stock_price is not None:
            print(f"{symbol}: {stock_price}")
        else:
            print(f"Failed to fetch real-time stock price for {symbol}")

    print("\nSimple Moving Average (SMA):")
    for symbol in stock_symbols:
        sma = get_sma_for_symbol(api_key, symbol)
        if sma is not None:
            print(f"{symbol}: {sma}")
        else:
            print(f"Failed to fetch SMA for {symbol}")