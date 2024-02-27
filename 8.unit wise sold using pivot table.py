import pandas as pd
import numpy as np
df = pd.read_csv('sales.csv')
print(pd.pivot_table(df,index=["Item"], values="Units", aggfunc=np.sum))
