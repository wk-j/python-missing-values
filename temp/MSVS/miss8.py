import pandas as pd
import os

# Create an indicator variable for "missing"
# column = pets
os.chdir("d:\\temp")
df = pd.read_csv('missing_values.csv')
df['party'] = df[['attending_party']].fillna(0)
print(df[['attending_party', 'party']])
print("end")
