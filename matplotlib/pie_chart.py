import numpy as np
import matplotlib.pyplot as plt

y = np.array([35, 25, 25, 15])
mylabels = np.array(["Apples", "Bananas", "Cherries", "Dates"])
myexplode = [0.2, 0, 0, 0]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels=mylabels, explode=myexplode, shadow=True, colors=mycolors)
plt.legend(title="Four Fruits")



plt.show()