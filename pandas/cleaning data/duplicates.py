import pandas as pd

df = pd.read_csv('pandas/cleaning data/data.csv')

print(df.duplicated())

df.drop_duplicates(inplace=True)
