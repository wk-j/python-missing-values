import pandas as pd
import os

# Replace missing values with a missing rank
# column = parking_space
os.chdir("d:\\temp")
df = pd.read_csv('missing_values.csv')
print(type(df))
print(list(df))
print(df[['name', 'age', 'parking_space']])
# Missing one might be 12
df['park1'] = df[['parking_space']].fillna(12)
print(df[['parking_space', 'park1']])
print("end")
print("***")
