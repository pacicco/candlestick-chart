
import matplotlib.pyplot as plt
import pandas as web
import mplfinance as mpf
import datetime as dt
import yfinance as yf


#importing stock data from Yahoo Finance
start = dt.datetime(2010, 1, 1)
end = dt.datetime.now()

#extract stock data without datareader
stock_data = yf.download('AAPL', start=start, end=end)

#plotting the stock data
mpf.plot(stock_data, type='candle', style='charles')
plt.plot(stock_data['Close'])
plt.show()