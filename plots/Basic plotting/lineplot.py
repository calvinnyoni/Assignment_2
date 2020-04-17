#Practicing line plotting
#Calvin Nyoni
#27 November 2019

import math
import matplotlib.pyplot as plt
import numpy as np

# x = 0
# y = 0

# x_axis_data = [] #x-axis points

# while x < 5:
#     x_axis_data.append(x)
#     x += 1

# x = 0

# linear_data = [] #linear function data

# while x < 5:
#     y = x
#     linear_data.append(y)
#     x += 1

# x = 0

# quadratic_data = [] #quadratic function data

# while x < 5:
#     y = math.pow(x, 2)
#     quadratic_data.append(y)
#     x += 1

# x = 0

# exponential_data = []  #exponential function data

# while x < 5:
#     y = math.exp(x)
#     exponential_data.append(y)
#     x += 1

# x = 1

# log_data = [] #logarithimic function data

# while x < 6:
#     y = math.log(x)
#     log_data.append(y)
#     x += 1

# plt.plot(x_axis_data, linear_data)
# plt.plot(x_axis_data, quadratic_data)
# plt.plot(x_axis_data, exponential_data)
# plt.plot(x_axis_data, log_data)

x = np.linspace(0,5, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x ** 3, label='cubic')
plt.plot(x, np.exp(x) , label='exponential')

plt.show()

print("Done")