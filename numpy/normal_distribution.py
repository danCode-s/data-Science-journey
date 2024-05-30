from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.normal(loc=1, scale=2, size=(2, 3))
sns.distplot(random.normal(size=100), hist=False)

print(x)
plt.show()