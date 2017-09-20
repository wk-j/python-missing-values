import pandas as pd
import os

# Delete columns that are missing too
# many values to be useful
# column = pets
os.chdir("d:\\temp")
df = pd.read_csv('missing_values.csv')
del df['pets']
print(df)
print("end")
