import pandas as pd
import os

# Create an indicator variable for "missing"
# column = pets
os.chdir("d:\\temp")
df = pd.read_csv('missing_values.csv')
df['pets1'] = df[['pets']].fillna(0)
df['pets2'] = df[['pets1']].isin([0])
print(df[['name', 'pets', 'pets1', 'pets2']])
print("end")
