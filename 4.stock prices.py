import pandas as pd
import matplotlib.pyplot as plt
stock_prices = pd.read_csv('C:/Users/manas/OneDrive/Documents/DSA0504/stock_prices.csv')
stock_prices['Date'] = pd.to_datetime(stock_prices['Date'])
start_date = '2023-01-01'
end_date = '2023-01-08'
filtered_stock_prices = stock_prices[(stock_prices['Date'] >= start_date) & (stock_prices['Date'] <= end_date)]
plt.figure(figsize=(10, 6))
plt.plot(filtered_stock_prices['Date'], filtered_stock_prices['Close'], marker='o', linestyle='-')
plt.title('Historical Stock Prices of Alphabet Inc. ({} to {})'.format(start_date, end_date))
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
