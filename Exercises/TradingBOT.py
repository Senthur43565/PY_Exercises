# import yfinance as cx
# import pandas as pd
# data = cx.download("EURUSD = X", start="2023-01-01", end = "2022-02-01", interval="15m")
# data.iloc[-1:,:]
# data.Open.iloc
# print(data)
# def signal_generator(df):
#     open = df.Open.iloc[-1]
#     close = df.Close.iloc[-1]
#     previous_open = df.Open.iloc[-2]
#     previous_close = df.Close.iloc[-2]

#     if (open > close and previous_open < previous_close and close < previous_open and open >= previous_close):
#         return 1
#     elif (open < close and previous_open > previous_close and close > previous_open and open <= previous_close):
#         return 2
#     else:
#         return 0

# signal = []
# signal .append(0)
# for i in range(1, len(data)):
#     df = data[i-1 : i+1]
#     signal.append(signal_generator(df))

# data["signal"] = signal
# data.signal.value_counts()

# from apscheduler.schedulers.blocking import BlockingScheduler
# from oandapyV20 import API
# import oandapyV20.endpoints.orders as orders
# from oandapyV20.contrib.requests import MarketOrderRequest
# from oanda_candles import Pair, Gran, CandleCollector, CandleClient
# from oandapyV20.contrib.requests import TakeProfitDetails, StopLossDetails

# from config import access_token, accountID
# def get_candles(n):
#     client = CandleClient(access_token, real=False)
#     collector = client.get_collector(Pair.EUR_USD, Gran.M15)
#     candles = collector.grab(n)
#     return candles
# candles = get_candles(3)
# for candle in candles:
#     print(float(str(candle.bid.o)) > 1)

# def trading_job():
#     candles = get_candles(3)
#     dfstream = pd.DataFrame(columns=['Open', 'Close', 'High', 'Low'])

#     i = 0
#     for candle in candles:
#         dfstream.loc[i, ['Open']] = float(str(candle.bid.o))
#         dfstream.loc[i, ['Close']] = float(str(candle.bid.c))
#         dfstream.loc[i, ['High']] = float(str(candle.bid.h))
#         dfstream.loc[i, ['Low']] = float(str(candle.bid.l))
#     dfstream['Open'] = dfstream['Open'].astype(float)
#     dfstream['Close'] = dfstream['Close'].astype(float)
#     dfstream['High'] = dfstream['High'].astype(float)
#     dfstream['Low'] = dfstream['Low'].astype(float)
#     signal = signal_generator(dfstream.iloc[:-1, :])
#     client = API(access_token)
#     SLTPRatio = 2.
#     previous_candleR = abs(dfstream['Open'].iloc[-2] - dfstream['Close'].iloc[-2])
#     SLBuy = float(str(candle.bid.o)) - previous_candleR
#     SLSell = float(str(candle.bid.o)) + previous_candleR
#     TPBuy = float(str(candle.bid.o)) + previous_candleR * SLTPRatio
#     TPSell = float(str(candle.bid.o)) - previous_candleR * SLTPRatio
#     print(dfstream.iloc[:-1, :])
#     print(TPBuy, " ", SLBuy, " ", TPSell, " ", SLSell)

#     if signal == 1:
#         mo = MarketOrderRequest(instrument= "EUR_USD", units= -1000, takeProfitOnFill = TakeProfitDetails(price = TPSell).data, stopLossOnFill = StopLossDetails(price=SLSell).data)
#         r = orders.OrderCreate(accountID, data=mo.data)
#         rv = client.request(r)
#         print(rv)
#     elif signal == 2:
#         mo = MarketOrderRequest(instrument= "EUR_USD", units=1000, takeProfitOnFill= TakeProfitDetails(price=TPBuy).data, stopLossOnFill=StopLossDetails(price=SLBuy).data)
#         r = orders.OrderCreate(accountID, data=mo.data)
#         rv = client.request(r)
#         print(rv)
# scheduler = BlockingScheduler()
# scheduler.add_job(trading_job, 'cron', day_of_week= 'mon-fri', hour = '00-23',minute = '1,16,31,46', start_date = '05-11-2023 12:00:00', timezone = 'India/Chennai')
# scheduler.start()






import ccxt
import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler

# Define your Binance API credentials
binance_api_key = 'Oyeqpb5ptubvJUK47UPvcwNFqId0S0F0Xlo1Wdn3YQKia4KptdG9PRkuguD1lqj4'
binance_api_secret = 'CgUGJCIWWrVZCbQiEL9Xq9aVD1ACorLKr3rvVR8WVtZxrIsM8kUyNkdAqU6YWZBc'

# Initialize the Binance exchange object
exchange = ccxt.binance({
    'apiKey': binance_api_key,
    'secret': binance_api_secret,
})

def get_candles(symbol, timeframe, limit):
    # Fetch candlestick data from Binance
    candles = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    return candles

def trading_job():
    symbol = 'EUR/USDT'  # Replace with your desired trading pair
    timeframe = '15m'    # Replace with your desired timeframe
    limit = 3

    candles = get_candles(symbol, timeframe, limit)
    dfstream = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    
    # Implement your trading strategy here
    i = 0
    for candle in candles:
        dfstream.loc[i, ['Open']] = float(str(candle.bid.o))
        dfstream.loc[i, ['Close']] = float(str(candle.bid.c))
        dfstream.loc[i, ['High']] = float(str(candle.bid.h))
        dfstream.loc[i, ['Low']] = float(str(candle.bid.l))
    dfstream['Open'] = dfstream['Open'].astype(float)
    dfstream['Close'] = dfstream['Close'].astype(float)
    dfstream['High'] = dfstream['High'].astype(float)
    dfstream['Low'] = dfstream['Low'].astype(float)
    signal = signal_generator(dfstream.iloc[:-1, :])
    client = API(access_token)
    SLTPRatio = 2.
    previous_candleR = abs(dfstream['Open'].iloc[-2] - dfstream['Close'].iloc[-2])
    SLBuy = float(str(candle.bid.o)) - previous_candleR
    SLSell = float(str(candle.bid.o)) + previous_candleR
    TPBuy = float(str(candle.bid.o)) + previous_candleR * SLTPRatio
    TPSell = float(str(candle.bid.o)) - previous_candleR * SLTPRatio
    print(dfstream.iloc[:-1, :])
    print(TPBuy, " ", SLBuy, " ", TPSell, " ", SLSell)

    if signal == 1:
        mo = MarketOrderRequest(instrument= "EUR_USD", units= -1000, takeProfitOnFill = TakeProfitDetails(price = TPSell).data, stopLossOnFill = StopLossDetails(price=SLSell).data)
        r = orders.OrderCreate(accountID, data=mo.data)
        rv = client.request(r)
        print(rv)
    elif signal == 2:
        mo = MarketOrderRequest(instrument= "EUR_USD", units=1000, takeProfitOnFill= TakeProfitDetails(price=TPBuy).data, stopLossOnFill=StopLossDetails(price=SLBuy).data)
        r = orders.OrderCreate(accountID, data=mo.data)
        rv = client.request(r)
        print(rv)
    # ...

scheduler = BlockingScheduler()
scheduler.add_job(trading_job, 'interval', minutes=15, max_instances=1)  # Replace with your desired scheduling
scheduler.start()






# import ccxt
# import pandas as pd
# import time
# from apscheduler.schedulers.blocking import BlockingScheduler

# # Create a ccxt exchange object
# exchange = ccxt.binance()

# # Convert the start date and time to a Unix timestamp in milliseconds
# start_date = "2023-01-01"
# start_time = "00:00:00"
# start_timestamp = pd.Timestamp(start_date + " " + start_time).timestamp() * 1000

# # Fix the startTime parameter
# start_timestamp = int(start_timestamp)

# # Download historical data for TRX/USDT
# data = exchange.fetch_ohlcv("TRX/USDT", timeframe='15m', since=start_timestamp, limit=1000)

# # Create a pandas DataFrame from the downloaded data
# df = pd.DataFrame(data, columns=['Open', 'High', 'Low', 'Close', 'Volume', 'QuoteVolume'])

# # Define the signal generator function
# def signal_generator(df):
#     open = df.Open.iloc[-1]
#     close = df.Close.iloc[-1]
#     previous_open = df.Open.iloc[-2]
#     previous_close = df.Close.iloc[-2]

#     if (open > close and previous_open < previous_close and close < previous_open and open >= previous_close):
#         return 1
#     elif (open < close and previous_open > previous_close and close > previous_open and open <= previous_close):
#         return 2
#     else:
#         return 0

# # Generate signals
# df['signal'] = df.apply(signal_generator, axis=1)

# # Define the trading job function
# def trading_job():
#     # Get the latest 3 candles
#     candles = exchange.fetch_ohlcv("TRX/USDT", timeframe='15m', limit=3)

#     # Create a pandas DataFrame from the latest 3 candles
#     dfstream = pd.DataFrame(candles, columns=['Open', 'High', 'Low', 'Close', 'Volume'])

#     # Generate signal for the latest 3 candles
#     signal = signal_generator(dfstream.iloc[:-1, :])

#     # Place a buy order if the signal is 1
#     if signal == 1:
#         try:
#             exchange.create_order("TRX/USDT", "market", "buy", 1000)
#             print("Placed a buy order for TRX/USDT")
#         except Exception as e:
#             print("Failed to place a buy order for TRX/USDT:", e)

#     # Place a sell order if the signal is 2
#     elif signal == 2:
#         try:
#             exchange.create_order("TRX/USDT", "market", "sell", 1000)
#             print("Placed a sell order for TRX/USDT")
#         except Exception as e:
#             print("Failed to place a sell order for TRX/USDT:", e)

# # Schedule the trading job to run every minute
# scheduler = BlockingScheduler()
# scheduler.add_job(trading_job, 'interval', seconds=60)
# scheduler.start()





# import ccxt
# import pandas as pd
# import time
# from apscheduler.schedulers.blocking import BlockingScheduler

# # Create a ccxt exchange object
# exchange = ccxt.binance()

# # Convert the start date and time to a Unix timestamp in milliseconds
# start_date = "2023-01-01"
# start_time = "00:00:00"
# start_timestamp = pd.Timestamp(start_date + " " + start_time).timestamp() * 1000

# # Fix the startTime parameter
# start_timestamp = int(start_timestamp)

# # Download historical data for TRX/USDT
# data = exchange.fetch_ohlcv("TRX/USDT", timeframe='15m', since=start_timestamp, limit=1000)




# # Create a pandas DataFrame from the downloaded data
# df = pd.DataFrame(data, columns=['Open', 'High', 'Low', 'Close', 'Volume'])

# # Define the signal generator function
# def signal_generator(df):
#     open = df.Open.iloc[-1]
#     close = df.Close.iloc[-1]
#     previous_open = df.Open.iloc[-2]
#     previous_close = df.Close.iloc[-2]

#     if (open > close and previous_open < previous_close and close < previous_open and open >= previous_close):
#         return 1
#     elif (open < close and previous_open > previous_close and close > previous_open and open <= previous_close):
#         return 2
#     else:
#         return 0

# # Generate signals
# df['signal'] = df.apply(signal_generator, axis=1)

# # Define the trading job function
# def trading_job():
#     # Get the latest 3 candles
#     candles = exchange.fetch_ohlcv("TRX/USDT", timeframe='15m', limit=3)

#     # Create a pandas DataFrame from the latest 3 candles
#     dfstream = pd.DataFrame(candles, columns=['Open', 'High', 'Low', 'Close', 'Volume'])

#     # Generate signal for the latest 3 candles
#     signal = signal_generator(dfstream.iloc[:-1, :])

#     # Place a buy order if the signal is 1
#     if signal == 1:
#         try:
#             exchange.create_order("TRX/USDT", "market", "buy", 1000)
#             print("Placed a buy order for TRX/USDT")
#         except Exception as e:
#             print("Failed to place a buy order for TRX/USDT:", e)

#     # Place a sell order if the signal is 2
#     elif signal == 2:
#         try:
#             exchange.create_order("TRX/USDT", "market", "sell", 1000)
#             print("Placed a sell order for TRX/USDT")
#         except Exception as e:
#             print("Failed to place a sell order for TRX/USDT:", e)

# # Schedule the trading job to run every minute
# scheduler = BlockingScheduler()
# scheduler.add_job(trading_job, 'interval', seconds=60)
# scheduler.start












import angelbroking
from apscheduler.schedulers.blocking import BlockingScheduler

# Create an Angel Broking API client
angelbroking_client = angelbroking.AngelBroking(client_id, access_token)

# Define the moving average periods
short_term_ma_period = 15
long_term_ma_period = 50

# Calculate the moving averages
def get_moving_averages(symbol):
  short_term_ma = angelbroking_client.get_moving_average(symbol, timeframe="15m", period=short_term_ma_period)
  long_term_ma = angelbroking_client.get_moving_average(symbol, timeframe="15m", period=long_term_ma_period)
  return short_term_ma, long_term_ma

# Identify the trend direction
def identify_trend_direction(short_term_ma, long_term_ma):
  trend_direction = 'up' if short_term_ma > long_term_ma else 'down'
  return trend_direction

# Identify the entry point
def identify_entry_point(trend_direction, short_term_ma, long_term_ma):
  if trend_direction == 'up' and short_term_ma > long_term_ma:
    entry_point = 'buy'
  elif trend_direction == 'down' and short_term_ma < long_term_ma:
    entry_point = 'sell'
  else:
    entry_point = None
  return entry_point

# Place a market order
def place_market_order(symbol, quantity):
  angelbroking_client.place_market_order(symbol, quantity)

# Trade based on the moving average crossover strategy
def trade_based_on_ma_crossover():
  symbol = 'EUR/USD'  # Replace with your desired trading pair

  # Get the moving averages
  short_term_ma, long_term_ma = get_moving_averages(symbol)

  # Identify the trend direction
  trend_direction = identify_trend_direction(short_term_ma, long_term_ma)

  # Identify the entry point
  entry_point = identify_entry_point(trend_direction, short_term_ma, long_term_ma)

  # Place a market order if there is an entry point
  if entry_point is not None:
    place_market_order(symbol, entry_point, 1000)

# Start the scheduler
scheduler = BlockingScheduler()
scheduler.add_job(trade_based_on_ma_crossover, 'interval', minutes=15, max_instances=1)
scheduler.start()
