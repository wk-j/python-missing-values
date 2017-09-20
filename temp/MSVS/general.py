import pandas as pd
import os

# General useful commands
os.chdir("d:\\temp")    # change current directory
# Read CSV to pandas Data frame
df = pd.read_csv('missing_values.csv')
print(type(df))     # show data type of df
print(list(df))     # show column list
print(df)           # show all rows & columns
# column projection limit
print(df[['name', 'age', 'income']])
# row limit
print(df[['name', 'age', 'income']].head(n=5))



