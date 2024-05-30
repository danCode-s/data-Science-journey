import pandas as pd

df_0 = pd.read_csv('pandas/basic/data.csv')

# Deafault: we cant print the whole csv as data frame 
# to print the whole csv - we convert df into string

print(df_0.to_string())

# max rows
print(pd.options.display.max_rows)

# increase the number of max rows to print the entire data frame

pd.options.display.max_rows = 9999

print(df_0)
