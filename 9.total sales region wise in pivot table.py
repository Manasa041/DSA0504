import pandas as pd
data = pd.read_csv("sales_data.csv")
table = pd.pivot_table(data, values='Sale_amt', index=['Region', 'Manager', 'SalesMan'], aggfunc=sum)
print(table)
