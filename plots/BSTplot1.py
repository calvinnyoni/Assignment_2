#Plotting binary search tree application search results
#Calvin Nyoni
#21 March 2020

import math
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(50, 2500, 10)

best_case_results = np.ones(10)

average_case_results = np.array([15.93, 19.86, 20.47, 22.62, 22.29, 21.50, 22.39, 24.26, 23.64, 25])

worst_case_results = np.array([29, 35, 45, 41, 51, 45, 45, 51, 45, 51])

# plt.plot(x, best_case_results, label = 'best case', color = [(1,179/255,186/255)],marker = 'o', linestyle = '-')
# plt.plot(x, average_case_results, label = 'average case', color = [(186/255,1,201/255)], marker = 'o', linestyle = '-')
# plt.plot(x, worst_case_results, label = 'worst case', color = [(186/255,1,1)], marker = 'o', linestyle = '-')

plt.plot(x, best_case_results, label = 'best case', color = '#ffe700' ,marker = 'o', linestyle = '-')
plt.plot(x, average_case_results, label = 'average case', color = '#00aedb', marker = 'o', linestyle = '-')
plt.plot(x, worst_case_results, label = 'worst case', color = '#a200ff', marker = 'o', linestyle = '-')

plt.ylim(0,60)

plt.xlabel('Sample Size (n)')
plt.ylabel('Number of Operations')

plt.legend()

plt.show()