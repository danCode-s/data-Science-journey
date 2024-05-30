import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print(myvar[0])

myvar_2 = pd.Series(a, index= ["x", "y", "z"])

print(myvar_2)

#Key/Value pairs - Dictionary
# keys become Labels

calories = {'day1': 420, 'day2': 360, 'day3':390}
myvar_3 = pd.Series(calories)
print(myvar_3)

# Series only from 'day1' and 'day2'
myvar_4 = pd.Series(calories, index = ['day1', 'day2'])
print(myvar_4)


# Data Frame
data = {
    'calories': [420, 360, 390], 
    'duration': [50, 40, 45]
}

myvar_5 = pd.DataFrame(data)
print(myvar_5)