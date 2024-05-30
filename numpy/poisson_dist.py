from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# sns.distplot(random.poisson(lam=2, size=1000), kde=False)
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

plt.show()