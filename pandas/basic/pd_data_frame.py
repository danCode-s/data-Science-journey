import pandas as pd

data = {
    "calories":[420, 360, 390],
    "duration":[50, 45, 40]

}

df = pd.DataFrame(data)


print(df)
print(df.loc[0])
print(df.loc[[0, 1]])

df0 = pd.DataFrame(data,  index=["day1", "day2", "day3"])
print(df0)
print(df0.loc["day1"])

#load files into DataFrame
df1 = pd.read_csv('data.csv')
print(df1)

print(df.to_string())
print(df1.head())
print(df1.tail())