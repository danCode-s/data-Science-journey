import pandas as pd

df = pd.read_json('pandas/basic/data.json')

print(df.to_string())

# Python dictionaries are same as json files so you can directly use them in the code