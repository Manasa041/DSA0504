import pandas as pd
import matplotlib.pyplot as plt
start_date = "2023-01-01"
end_date = "2023-01-08"
data = pd.read_csv("stock_prices.csv", index_col="Date", parse_dates=True)
data = data.loc[(data.index >= start_date) & (data.index <= end_date)]
plt.figure(figsize=(10, 6))
plt.scatter(data["Close"], data["Volume"], alpha=0.5)
plt.title("Alphabet Inc. Stock Price vs. Trading Volume")
plt.xlabel("Closing Price")
plt.ylabel("Trading Volume")
plt.grid(True)
plt.show()
