import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random


x = random.zipf(a=2, size=1000)
sns.histplot(x[x<10])
plt.show()