#Practicing plotting statistical distributions
#Calvin Nyoni
#2 December 2019

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter

#average and standard deviation
mu_avg = 50
sigma_stddev = 10

#data
data_points_1 = mu_avg + (sigma_stddev * np.random.randn(1000))

plt.figure()  #figure where all plots will be plotted

plt.subplot(221)  #1st subplot

plt.hist(data_points_1, 50, density=1, color='green', alpha=0.75)

#plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Normal distribution')
plt.grid(True)



plt.subplot(222)  #2nd subplot

#data
data_points_2 = np.random.binomial(100, 0.5, 100)

plt.hist(data_points_2, 50, density=1, color='blue', alpha=0.75)

#plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Binomial distribution')
plt.grid(True)

plt.subplot(223)  #3rd subplot

#data
data_points_3 = np.random.exponential(5,100)

plt.hist(data_points_3, 50, density=1, color='red', alpha=0.75)

#plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Exponential distribution')
#plt.grid(True)

plt.subplot(224)  #3rd subplot

#data
data_points_4 = np.random.poisson(10, 100)

plt.hist(data_points_4, 50, density=1, color='yellow', alpha=0.75)

#plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Poisson distribution')
#plt.grid(True)

# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
wspace=0.35)

plt.show()