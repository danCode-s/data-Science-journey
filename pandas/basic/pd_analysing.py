import pandas as pd

# The head() method returns the headers and a specified number of rows, starting from the top.

df = pd.read_csv('pandas/basic/data.csv')


#print the first ten rows of the data Frame
# Default: 5 rows

print(df.head(10))

# printing the last rows

print(df.tail())


# more info about the data Frame

print(df.info())
