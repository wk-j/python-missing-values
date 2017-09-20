import pandas as pd
import os

# Replace missing values with a constant
# column = income
os.chdir("d:\\temp")
df = pd.read_csv('missing_values.csv')
print(type(df))
print(list(df))
print(df[['name', 'age', 'income']])
df['income1'] = df[['income']].fillna(250)
print(df[['income', 'income1']])
print("end")
print("***")
