# Basics
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime

# Select the 505 stocks of SP500 plus the SP500 itself
tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
stocks = tables[0].Symbol.values.tolist() + ['^GSPC']
stocks = [s.replace('.', '-') for s in stocks]

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
df.to_csv('data/SP500_stocks_2000_2019.csv')