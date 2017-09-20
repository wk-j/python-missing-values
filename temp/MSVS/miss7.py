import pandas as pd
import os

# Replace missing values with a dummy
# column = parking_space
os.chdir("d:\\temp")
df = pd.read_csv('missing_values.csv')
print(type(df))
print(list(df))
print(df[['name', 'age', 'parking_space']])
# dummy is -99
df['park1'] = df[['parking_space']].fillna(-99)
print(df[['parking_space', 'park1']])
print("end")
print("***")
