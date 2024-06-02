import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('pandas/plotting/data.csv')

# df.plot()

# Scatter Plot
# df.plot(kind='scatter', x='Duration', y='Calories')
# df.plot(kind='scatter', x='Duration', y='Maxpulse')


# HISTOGRAM
'''
Use the kind argument to specify that you want a histogram:

kind = 'hist'

A histogram needs only one column.

A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?
'''

df['Duration'].plot(kind='hist')

plt.show()