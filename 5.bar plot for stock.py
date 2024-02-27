import pandas as pd
import matplotlib.pyplot as plt
stock_prices = pd.read_csv('stock_prices.csv')
stock_prices['Date'] = pd.to_datetime(stock_prices['Date'])
start_date = '2023-01-01'
end_date = '2023-01-07'
filtered_stock_prices = stock_prices[(stock_prices['Date'] >= start_date) & (stock_prices['Date'] <= end_date)]
plt.figure(figsize=(10, 6))
plt.bar(filtered_stock_prices['Date'], filtered_stock_prices['Volume'], color='skyblue')
plt.title('Trading Volume of Alphabet Inc. Stock ({} to {})'.format(start_date, end_date))
plt.xlabel('Date')
plt.ylabel('Volume')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
