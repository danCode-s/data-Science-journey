from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns

x = random.rayleigh(scale=2, size=(2, 3))

print(x)

sns.kdeplot(random.rayleigh(size=1000))


plt.show()