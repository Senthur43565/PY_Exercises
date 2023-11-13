import requests
import json
import hmac
import hashlib

API_KEY = "Oyeqpb5ptubvJUK47UPvcwNFqIdOSOFOXlo1Wdn3YQKia4KptdG9PRkuguD1lqj4"
API_SECRET = "CgUGJCIWWrVZCbQiEL9Xq9aVD1ACorLkr3rvVR8WVtZXrIsM8kUyNkdAqU6YWZBC"

def fetch_account_info():
    # Define the endpoint for account information
    endpoint = "https://api.binance.com/api/v3/account"

    # Prepare the request with headers
    headers = {
        "X-MBX-API-KEY": API_KEY,
    }

    # Generate the signature
    order_params = {}  # Define the order parameters
    query_string = "&".join([f"{key}={value}" for key, value in order_params.items()])
    signature = hmac.new(API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    # Add the signature to the headers
    headers['X-MBX-API-SIGNATURE'] = signature

    # Send the GET request to fetch account information
    response = requests.get(endpoint, headers=headers)

    # Check the response
    if response.status_code == 200:
        account_info = response.json()
        print("Account Information:")
        print(json.dumps(account_info, indent=2))
    else:
        print("Error:", response.status_code, response.text)

def place_test_order():
    # Define the order parameters (symbol, side, type, quantity, etc.)
    order_params = {
        "symbol": "BTCUSDT",  # Add the symbol parameter
        "side": "BUY",  # Change to "SELL" for a sell order
        "type": "MARKET",
        "quantity": 1,  # Adjust the quantity as needed
    }

    # Define the endpoint for placing a test order
    endpoint = "https://testnet.binance.vision/api/v3/order/test"

    # Prepare the request with headers
    headers = {
        "X-MBX-API-KEY": API_KEY,
    }

    # Generate the signature
    query_string = "&".join([f"{key}={value}" for key, value in order_params.items()])
    signature = hmac.new(API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    # Add the signature to the headers
    headers['X-MBX-API-SIGNATURE'] = signature

    # Send the POST request to place a test order
    response = requests.post(endpoint, headers=headers, json=order_params)

    # Check the response
    if response.status_code == 200:
        print("Test order placed successfully.")
    else:
        print("Error:", response.status_code, response.text)

print("Starting Binance API Script")

# Call the functions to fetch account information and place a test order
fetch_account_info()
place_test_order()

print("Binance API Script Completed")
