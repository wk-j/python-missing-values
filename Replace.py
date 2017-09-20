import pandas as pd
import os

# Replace missing values with the mean (age)
# column = age
os.chdir("data")

df = pd.read_csv('MissingValues.csv')

'''
print(type(df))
print(list(df))
print(df[['name', 'age', 'income']])
'''

# replace missing value with mean
# and create a new column 'age1'

#df['age1'] = df[['age']].fillna(df.mean()['age':'age'])
df['age1'] = df[['age']].fillna(df.median()['age':'age'])


'''
k = df.mean()["age":"income"]
print("mean", df.mean())
print("age:age", k)
print("age:age", df.mean()["age"])
'''

print(df[['age', 'age1']])
#print("end")
#print("***")