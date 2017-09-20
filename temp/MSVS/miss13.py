import pandas as pd
import os

# Delete row that are missing too
# many values to be useful
os.chdir("d:\\temp")
df = pd.read_csv('missing_values.csv')
df = df.dropna(how='any')   # 'all'
print(df)
print("end")
