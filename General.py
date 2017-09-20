
import pandas as pd
import os

# General useful commands
os.chdir("data")    # change current directory
# Read CSV to pandas Data frame


def join (r) :
    return r["name"] + "   " + str(r["age"])
    #return r["name"]


df = pd.read_csv('MissingValues.csv')

'''
print(type(df))     # show data type of df
print(list(df))     # show column list
print(df)           # show all rows & columns
# column projection limit
print(df[['name', 'age', 'income']])
# row limit
print(df[['name', 'age', 'income']].head(n=5))
'''


x = df.apply(join, axis=1)
print(x)