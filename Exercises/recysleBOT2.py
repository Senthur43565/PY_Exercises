import requests
import json
from datetime import datetime, timedelta
import time
from queue import Queue
import logging
from functools import lru_cache
import os

API_KEY = os.environ.get("BINANCE_API_KEY")
API_SECRET = os.environ.get("BINANCE_API_SECRET")


# # Replace these with your API key and secret
# API_KEY = "Oyeqpb5ptubvJUK47UPvcwNFqId0S0F0Xlo1Wdn3YQKia4KptdG9PRkuguD1lqj4"
# API_SECRET = "CgUGJCIWWrVZCbQiEL9Xq9aVD1ACorLkr3rvVR8WVtZxrIsM8kUyNkdAqU6YWZBc"

# Define the moving average periods
SHORT_TERM_MA_PERIOD = 10
LONG_TERM_MA_PERIOD = 30

# Define the risk percentage per trade
RISK_PERCENTAGE = 0.02  # 2% risk per trade

# Define the take profit and stop loss percentages
TAKE_PROFIT_PERCENTAGE = 0.02  # 2% take profit
STOP_LOSS_PERCENTAGE = 0.01  # 1% stop loss

trading_pairs = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]

# Define a queue to store the requests
request_queue = Queue()


# Define a function to fetch the current price with caching
@lru_cache(maxsize=None)
def get_current_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        return float(data["price"])
    else:
        raise Exception("Error getting price:", response.content)


# Calculate the moving average
def calculate_moving_averages(symbol):
    # Get the latest historical data for the symbol
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=15m"

    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)

        # Calculate the short-term and long-term moving averages
        short_term_ma = sum([float(
            candle[4]) for candle in data[-SHORT_TERM_MA_PERIOD::]]) / SHORT_TERM_MA_PERIOD
        long_term_ma = sum(
            [float(candle[4]) for candle in data[-LONG_TERM_MA_PERIOD::]]) / LONG_TERM_MA_PERIOD

        return short_term_ma, long_term_ma
    else:
        raise Exception("Error getting historical data:", response.content)

# Place a market order


def place_market_order(symbol, side, quantity, price=None):
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
    if price:
        payload["price"] = price
    response = requests.post(url, headers=headers, json=payload)

# Calculate the position size based on risk percentage per trade


def calculate_position_size(symbol, risk_percentage):
    # Get the current price of the desired trading pair
    current_price = get_current_price(symbol)

    # Calculate the position size based on risk percentage
    account_balance = 10000  # Replace with your actual account balance
    risk_amount = account_balance * risk_percentage
    position_size = risk_amount / current_price

    return position_size


# Configure the logging system
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Monitor the market and place trades based on the moving average crossover strategy


def monitor_market():
    for symbol in trading_pairs:
        current_price = get_current_price(symbol)
        short_term_ma, long_term_ma = calculate_moving_averages(symbol)
        trend_direction = "up" if short_term_ma > long_term_ma else "down"

        # Place a trade if there is an entry point
        if trend_direction == "up":
            # Calculate the position size based on risk percentage
            position_size = calculate_position_size(symbol, RISK_PERCENTAGE)

            # Place a buy order with the calculated position size
            place_market_order(symbol, "BUY", position_size)

            # Calculate the take profit and stop loss prices
            take_profit_price = current_price + \
                (current_price * TAKE_PROFIT_PERCENTAGE)
            stop_loss_price = current_price - \
                (current_price * STOP_LOSS_PERCENTAGE)

            # Place take profit and stop loss orders
            place_market_order(
                symbol, "SELL", position_size, take_profit_price)
            place_market_order(symbol, "SELL", position_size, stop_loss_price)

        elif trend_direction == "down":
            # Calculate the position size based on risk percentage
            position_size = calculate_position_size(symbol, RISK_PERCENTAGE)

            # Place a sell order with the calculated position size
            place_market_order(symbol, "SELL", position_size)

# Function to check for a bullish engulfing pattern


def is_bullish_engulfing(candle1, candle2):
    # Check if the first candle is bearish and the second candle is bullish
    if candle1['close'] < candle1['open'] and candle2['close'] > candle2['open']:
        # Check if the second candle engulfs the first candle
        if candle2['open'] < candle1['close'] and candle2['close'] > candle1['open']:
            return True
    return False

# Function to check for a bearish engulfing pattern


def is_bearish_engulfing(candle1, candle2):
    # Check if the first candle is bullish and the second candle is bearish
    if candle1['close'] > candle1['open'] and candle2['close'] < candle2['open']:
        # Check if the second candle engulfs the first candle
        if candle2['open'] > candle1['close'] and candle2['close'] < candle1['open']:
            return True
    return False

# Function to analyze candlestick patterns


def analyze_candlestick_patterns(data):
    # Iterate over the historical data
    for i in range(1, len(data)):
        # Get the current and previous candles
        current_candle = data[i]
        previous_candle = data[i-1]

        # Check for bullish engulfing pattern
        if is_bullish_engulfing(previous_candle, current_candle):
            print("Bullish engulfing pattern detected!")

        # Check for bearish engulfing pattern
        if is_bearish_engulfing(previous_candle, current_candle):
            print("Bearish engulfing pattern detected!")


# Backtesting component
def backtest_strategy(trading_pairs, start_date, end_date):
    for symbol in trading_pairs:
        # Convert start_date and end_date to milliseconds since the Unix epoch
        start_date = int(datetime.strptime(
            start_date, "%Y-%m-%d").timestamp() * 1000)
        end_date = int(datetime.strptime(
            end_date, "%Y-%m-%d").timestamp() * 1000)

        # Get historical data for the specified symbol and date range
        url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=15m&startTime={start_date}&endTime={end_date}"
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content)

            # Initialize variables for tracking performance
            total_trades = 0
            winning_trades = 0
            losing_trades = 0
            total_profit = 0

            # Iterate over the historical data
            for i in range(len(data)):
                # Calculate the moving averages
                short_term_ma, long_term_ma = calculate_moving_averages(symbol)

                # Identify the trend direction
                trend_direction = "up" if short_term_ma > long_term_ma else "down"

                # Simulate a trade based on the trend direction
                if trend_direction == "up" and short_term_ma < long_term_ma:
                    # Calculate the position size based on risk percentage
                    position_size = calculate_position_size(
                        symbol, RISK_PERCENTAGE)

                    # Simulate a buy order
                    entry_price = float(data[i][4])
                    take_profit_price = entry_price + \
                        (entry_price * TAKE_PROFIT_PERCENTAGE)
                    stop_loss_price = entry_price - \
                        (entry_price * STOP_LOSS_PERCENTAGE)

                    # Check if the take profit or stop loss is hit
                    for j in range(i+1, len(data)):
                        high_price = float(data[j][2])
                        low_price = float(data[j][3])

                        if high_price >= take_profit_price:
                            # Take profit hit
                            profit = take_profit_price - entry_price
                            total_profit += profit
                            winning_trades += 1
                            total_trades += 1
                            break
                        elif low_price <= stop_loss_price:
                            # Stop loss hit
                            loss = entry_price - stop_loss_price
                            total_profit -= loss
                            losing_trades += 1
                            total_trades += 1
                            break

                elif trend_direction == "down" and short_term_ma > long_term_ma:
                    # Calculate the position size based on risk percentage
                    position_size = calculate_position_size(
                        symbol, RISK_PERCENTAGE)

                    # Simulate a sell order
                    entry_price = float(data[i][4])
                    take_profit_price = entry_price - \
                        (entry_price * TAKE_PROFIT_PERCENTAGE)
                    stop_loss_price = entry_price + \
                        (entry_price * STOP_LOSS_PERCENTAGE)

                    # Check if the take profit or stop loss is hit
                    for j in range(i+1, len(data)):
                        high_price = float(data[j][2])
                        low_price = float(data[j][3])

                        if low_price <= take_profit_price:
                            # Take profit hit
                            profit = entry_price - take_profit_price
                            total_profit += profit
                            winning_trades += 1
                            total_trades += 1
                            break
                        elif high_price >= stop_loss_price:
                            # Stop loss hit
                            loss = stop_loss_price - entry_price
                            total_profit -= loss
                            losing_trades += 1
                            total_trades += 1
                            break

            # Calculate performance metrics
            win_rate = winning_trades / total_trades * 100
            average_profit = total_profit / total_trades

            # Print performance metrics
            print(f"Total Trades: {total_trades}")
            print(f"Winning Trades: {winning_trades}")
            print(f"Losing Trades: {losing_trades}")
            print(f"Win Rate: {win_rate}%")
            print(f"Average Profit: {average_profit}")

        else:
            raise Exception("Error getting historical data:", response.content)

# Function to handle rate limit exceeded error


def handle_rate_limit_error(response):
    if response.status_code == 429:
        # Rate limit exceeded, add the request to the queue
        request_queue.put(response.request)
        # Get the rate limit headers from the response
        rate_limit_headers = response.headers.get("x-mbx-used-weight-1m")
        if rate_limit_headers:
            # Extract the rate limit information
            rate_limit_info = rate_limit_headers.split("/")
            requests_remaining = int(rate_limit_info[0])
            time_window = int(rate_limit_info[1])
            # Calculate the delay for throttling
            delay = time_window / requests_remaining
            # Sleep for the calculated delay
            time.sleep(delay)
            # Return to exit the function after handling the rate limit error
            return
    # Other error occurred, raise an exception
    raise Exception("Error:", response.content)


# Function to process the requests in the queue
def process_request_queue():
    while not request_queue.empty():
        request = request_queue.get()
        response = requests.request(
            request.method, request.url, **request.kwargs)
        if response.status_code == 200:
            # Request successful, continue processing
            pass
        else:
            # Error occurred, handle the error
            handle_rate_limit_error(response)


# Start the bot
if __name__ == "__main__":
    while True:
        try:
            monitor_market()
            process_request_queue()
            time.sleep(15)
        except Exception as e:
            # Handle any other exceptions gracefully
            print("Error:", str(e))
            time.sleep(1)
