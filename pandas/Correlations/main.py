import pandas as pd 

# corr() --> Calculates the relationship betweeen each column in your data set

df = pd.read_csv('pandas/Correlations/data.csv')

print(df.corr())

'''
The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.

The number varies from -1 to 1.

1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.

0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.

-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.

0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.

GOOD CORRELATION --> atleast(0.6, -0.6)
PERFECT CORRELATION --> 1.00
GOOD CORRELATION in This Data set --> 0.922717 (Duration and Calories)
BAD CORRELATION in This Data Set --> 0.009403 (Duration and Maxpulse)
'''

