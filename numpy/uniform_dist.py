from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns


sns.kdeplot(random.uniform(size=1000), bw_adjust=0.5)

plt.show()