import pandas as pd
import os

# Replace missing values with the mean (age)
# column = age
os.chdir("d:\\temp")    # change current directory
df = pd.read_csv('missing_values.csv')  # Read CSV to pandas Data fra
print(type(df))     # show data type of df
print(list(df))
print(df[['name', 'age', 'income']])
df['age1'] = df[['age']].fillna(df.mean()['age':'age'])
print(df[['age', 'age1']])
print("end")
print("***")


