import pandas as pd
# World alcohol consumption data
w_a_con = pd.read_csv('world_alochol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print('\nShape of the dataframe: ',w_a_con.shape)
print('\nNumber of rows: ',w_a_con.shape[0])
print('\nNumber of column: ',w_a_con.shape[1])
print("\nExtract Column Names:")
print(w_a_con.columns)
