import pandas as pd
import os

# Replace missing values with the median
# column = age
os.chdir("d:\\temp")
df = pd.read_csv('missing_values.csv')
print(type(df))
print(list(df))
print(df[['name', 'age', 'income']])
df['age1'] = df[['age']].fillna(df.median()['age':'age'])
print(df[['age', 'age1']])
print("end")
print("***")
