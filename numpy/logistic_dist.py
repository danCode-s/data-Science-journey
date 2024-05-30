from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)


sns.kdeplot(random.logistic(size=1000), label='logistic')
sns.kdeplot(random.normal(scale=2, size=1000), label='normal')
plt.legend()
plt.show()
