import pandas as pd
import os

# Replace missing values with a string
# column = emergency_contact
os.chdir("d:\\temp")
df = pd.read_csv('missing_values.csv')
df['e1'] = df[['emergency_contact']].fillna('no')
print(df[['emergency_contact', 'e1']])
print("end")
