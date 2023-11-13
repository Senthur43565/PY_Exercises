import pandas as pd
import arch
import requests
import json
import websocket
import threading

# Define your Binance API credentials
api_key = 'Oyeqpb5ptubvJUK47UPvcwNFqIdOSOFOXlo1Wdn3YQKia4KptdG9PRkuguD1lqj4'
api_secret = 'CgUGJCIWWrVZCbQiEL9Xq9aVD1ACorLkr3rvVR8WVtZXrIsM8kUyNkdAqU6YWZBC'

# Set the symbol (e.g., ETHUSDT), interval (e.g., 15m for 15-minute data), and limit (number of data points)
symbol = 'ETHUSDT'
interval = '1h'
limit = 100  # Adjust the limit as needed to get the desired amount of historical data

# Function to retrieve historical data
def get_historical_data():
    base_url = 'https://api.binance.com/api/v1/klines'
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }
    response = requests.get(base_url, params=params, headers={'X-MBX-APIKEY': api_key})

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume", "close_time",
              "quote_asset_volume", "number_of_trades", "taker_buy_base_asset_volume",  "taker_buy_quote_asset_volume",   "ignore"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        df.set_index("timestamp", inplace=True)

        # Convert 'close' column to numeric, handling 'None' values
        df['close'] = pd.to_numeric(df['close'], errors='coerce')

        # Drop rows with missing or invalid 'close' values
        df.dropna(subset=['close'], inplace=True)

        # Calculate returns based on the cleaned 'close' prices
        df['returns'] = df['close'].pct_change()

        # Rescale the 'returns' column by a factor of 1000
        df['returns'] = 1000 * df['returns']

        # Create a GARCH(1,1) model
        model = arch.arch_model(df['returns'].dropna(), vol='Garch', p=1, q=1)

        # Fit the GARCH model to the data
        results = model.fit()

        # Print the summary of the GARCH model results
        print(results.summary())

        # Print the 'df' DataFrame with OHLCV data
        print(df)
    else:
        print("API request failed with status code:", response.status_code)

# Function to handle real-time WebSocket data
def handle_realtime_data():
    def on_message(ws, message):
        data = json.loads(message)
        # Extract the timestamp from the WebSocket data
        timestamp = pd.to_datetime(data['T'], unit='ms')
        # Process the live data along with the timestamp
        print(f"Timestamp: {timestamp}, Data: {data}")  

    def on_error(ws, error):
        print(f"Error: {error}")

    def on_close(ws, close_status_code, close_msg):
        print("Closed")

    def on_open(ws):
        # Subscribe to a symbol's trade stream
        payload = {
            "method": "SUBSCRIBE",
            "params": [
                f"{symbol}@trade"
            ],
            "id": 1
        }
        ws.send(json.dumps(payload))

    url = f"wss://stream.binance.com:9443/ws/{symbol.lower()}@trade"
    ws = websocket.WebSocketApp(url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open

    # Create a separate thread to run the WebSocket
    ws_thread = threading.Thread(target=ws.run_forever)
    ws_thread.daemon = True
    ws_thread.start()

if __name__ == "__main__":
    # Create a thread to handle real-time data
    realtime_thread = threading.Thread(target=handle_realtime_data)
    realtime_thread.start()

    # Start the historical data retrieval and processing in a separate thread
    historical_thread = threading.Thread(target=get_historical_data)
    historical_thread.start()

    # You can continue your program or keep it running to receive real-time data
