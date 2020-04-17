#Practicing scatter plotting
#Calvin Nyoni
#30 November 2019

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100, 4)
a_points = x + 10 * np.random.randn(25)
b_points = np.random.randint(25, 50, 25)
c_points = np.random.randint(50, 75, 25)
# d_points = np.random.randint(75, 100, 25)

plt.scatter(x, a_points, b_points, c_points)
#plt.scatter(x, b_points)
#plt.scatter(x, c_points)

plt.show()