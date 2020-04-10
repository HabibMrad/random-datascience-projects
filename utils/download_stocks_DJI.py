# Basics
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime

# Select the 505 stocks of SP500 plus the SP500 itself
stocks = ['MMM', 'AXP', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO', 'DOW', 'XOM', 
           'GS', 'HD', 'IBM', 'INTC', 'JNJ', 'JPM', 'MCD', 'MRK', 'MSFT', 'NKE', 
           'PFE', 'PG', 'RTX', 'TRV', 'UNH', 'VZ', 'V', 'WMT', 'WBA', 'DIS']
stocks = stocks + ['^DJI']

# Select the dates 
date_start = datetime(2000, 1, 1)
date_end   = datetime(2019, 12, 31)

# Import data from Yahoo Finance
df = pdr.get_data_yahoo(symbols = stocks, start = date_start, end = date_end)

# Keep only closing prices
df = df[['Close']]

# Delete annoying labels
df.columns = df.columns.get_level_values(1)
df.columns.name = None
df.index.name = None

# Save the data
df.to_csv('data/DJI_stocks_2000_2019.csv')