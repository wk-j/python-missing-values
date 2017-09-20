import pandas as pd
import os

# Replace missing values with the mean (age)
# column = age
os.chdir("d:\\temp")
df = pd.read_csv('missing_values.csv')
print(type(df))
print(list(df))
print(df[['name', 'age', 'income']])
# replace missing value with mean
# and create a new column 'age1'
df['age1'] = df[['age']].fillna(df.mean()['age':'age'])
print(df[['age', 'age1']])
print("end")
print("***")


