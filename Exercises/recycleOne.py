import requests
import json
from datetime import datetime, timedelta
import time
import binance
import asyncio
import websockets

# Replace these with your API key and secret
API_KEY = "Oyeqpb5ptubvJUK47UPvcwNFqId0S0F0Xlo1Wdn3YQKia4KptdG9PRkuguD1lqj4"
API_SECRET = "CgUGJCIWWrVZCbQiEL9Xq9aVD1ACorLkr3rvVR8WVtZxrIsM8kUyNkdAqU6YWZBc"

# Create a Binance client
client = binance.Client(API_KEY, API_SECRET)

# Define the moving average periods
SHORT_TERM_MA_PERIOD = 5 * 60  # 5 minutes
LONG_TERM_MA_PERIOD = 15 * 60

# Define the take profit and stop loss percentages
TAKE_PROFIT_PERCENTAGE = 0.01
STOP_LOSS_PERCENTAGE = 0.02

# Get the current price of the desired trading pair
def get_current_price(symbol):
    url = "https://api.binance.com/api/v3/ticker/price?symbol={}".format(symbol)
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        return float(data["price"])
    else:
        raise Exception("Error getting price:", response.content)

# Calculate the moving averages
def calculate_moving_averages(symbol):
    # Get the latest historical data for the symbol
    url = "https://api.binance.com/api/v3/klines?symbol=TRXUSDT&interval=15m".format(symbol)

    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)

        # Calculate the short-term and long-term moving averages
        short_term_ma = sum([float(candle[4]) for candle in data[-SHORT_TERM_MA_PERIOD::]]) / SHORT_TERM_MA_PERIOD
        long_term_ma = sum([float(candle[4]) for candle in data[-LONG_TERM_MA_PERIOD::]]) / LONG_TERM_MA_PERIOD

        return short_term_ma, long_term_ma
    else:
        raise Exception("Error getting historical data:", response.content)

# Place a market order
def place_market_order(symbol, side, quantity):
    url = "https://api.binance.com/api/v3/order"
    headers = {
        "X-MBX-API-KEY": API_KEY
    }
    payload = {
        "symbol": symbol,
        "type": "MARKET",
        "side": side,
        "quantity": quantity
    }
    response = requests.post(url, headers=headers, json=payload)

# Monitor the market and place trades based on the moving average crossover strategy
def monitor_market():
  # Get the current price of the desired trading pair
  symbol = "TRXUSDT"
  current_price = get_current_price(symbol)

  # Calculate the moving averages
  short_term_ma, long_term_ma = calculate_moving_averages(symbol)

  # Identify the trend direction
  trend_direction = "up" if short_term_ma > long_term_ma else "down"

  # Place a trade if there is an entry point
  if trend_direction == "up" and short_term_ma < long_term_ma:
    # Place a buy order
    place_market_order(symbol, "BUY", 100)

    # Calculate the take profit and stop loss prices
    take_profit_price = current_price + (current_price * TAKE_PROFIT_PERCENTAGE)
    stop_loss_price = current_price - (current_price * STOP_LOSS_PERCENTAGE)

    # Place take profit and stop loss orders
    place_market_order(symbol, "SELL", 100, take_profit_price)
    place_market_order(symbol, "SELL", 100, stop_loss_price)

    # Log the trade to the console
    print("Placed a buy order for 100 TRXUSDT at {}.".format(current_price))

  elif trend_direction == "down" and short_term_ma > long_term_ma:
    # Place a sell order
    place_market_order(symbol, "SELL", 100)
    print("Placed a sell order for 100 TRXUSDT at {}.".format(current_price))

async def subscribe_to_market_data():
    async with websockets.connect("wss://stream.binance.com:9443y/ws/trxusdt@trade") as websocket:
        while True:
            response = await websocket.recv()
            data = json.loads(response)
            print("Received data:", data)

# Start the bot
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(subscribe_to_market_data())
