import pandas as pd
import os

# Add an indicator variable showing which
# strings are considered "missing."
# column = emergency_contact
os.chdir("d:\\temp")
df = pd.read_csv('missing_values.csv')
k = ['NA', 'n/a', 'None', 'empty', '_', '""', 'null']
df['e1'] = df[['emergency_contact']].isin(k)
print(df[['name', 'emergency_contact', 'e1']])
print("end")
