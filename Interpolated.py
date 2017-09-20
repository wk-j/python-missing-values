import pandas as pd
import os

# Replace missing values with an interpolated estimate
# column = years_seniority
os.chdir("data")
df = pd.read_csv('MissingValues.csv')

print(type(df))
print(list(df))
print(df[['name', 'age', 'years_seniority']])
df['years_seniority1'] = df[['years_seniority']].fillna(11.5)
print(df[['years_seniority', 'years_seniority1']])
print("end")
print("***")