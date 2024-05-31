import pandas as pd

# ************* THIS CODE DOESNT WORK *****************
# Read the CSV file into a DataFrame
df = pd.read_csv('pandas/cleaning data/data.csv')

# Convert the 'Date' column to datetime format, handling both quoted and unquoted dates
df['Date'] = pd.to_datetime(df['Date'])

# Print the entire DataFrame
print(df.to_string())

