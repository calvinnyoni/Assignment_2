#Practicing trig plotting
#Calvin Nyoni
#30 November 2019

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1.0, 1.0, 0.01)
#x = np.arange(0, 2, 1)

plt.figure() #figure where all plots will be

plt.subplot(211)  #1st subplot
plt.plot(x, np.cos(2 * x * np.pi), color='r', linestyle = 'dashed')

plt.subplot(212)  #2nd subplot
plt.plot(x, np.sin(2 * x * np.pi), color='b', linestyle='dotted')

plt.show()
