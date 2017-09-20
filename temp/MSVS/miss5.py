import mice
import pandas as pd
import os
import numpy as np

os.chdir("d:\\temp")
df = pd.read_csv('missing_values.csv')
df2 = df[['age', 'years_seniority', 'income']]
a = np.array(df2)
x = mice.MICE().complete(a)
print(df2)
print('----------------')
print(x)
