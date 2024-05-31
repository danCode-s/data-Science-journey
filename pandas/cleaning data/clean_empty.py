import pandas as pd

df = pd.read_csv('pandas/cleaning data/data.csv')

# remove empty rows

df.dropna(inplace=True)

print(df.to_string())

# replace empty values
df1 = pd.read_csv('pandas/cleaning data/data.csv')

df1.fillna(130, inplace=True)
print(df1.to_string())

# Replace only for specified Column
df2 = pd.read_csv('pandas/cleaning data/data.csv')

df2['Calories'].fillna(130, inplace=True)
print(df2.to_string())


# replace using mean, median or mode 
# MEAN = Average
df3 = pd.read_csv('pandas/cleaning data/data.csv')

x = df3['Calories'].mean()
df3["Calories"].fillna(x, inplace=True)
print(df3.to_string())

# Median = the value in the middle, after sorting in ascending order 
df4 = pd.read_csv('pandas/cleaning data/data.csv')
y = df4["Calories"].median()
print(y)
df4['Calories'].fillna(y, inplace=True)
print(df4.to_string())


# Mode = value that appears most frequently
df5 = pd.read_csv('pandas/cleaning data/data.csv')
z = df5["Calories"].mode()[0]
df5["Calories"].fillna(z, inplace=True)
print(df5.to_string())
print(z)
