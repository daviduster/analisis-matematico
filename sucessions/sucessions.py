import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(0, 5, 100)

# setting the axes at the centre
fig = plt.figure()

# plot the functions
n = 1
plt.plot(x, (2*n*x**2)/(1 + (n**2)*x**4), 'b', label='n='+str(n))
n = 2
plt.plot(x, (2*n*x**2)/(1 + (n**2)*x**4), 'r', label='n='+str(n))
n = 3
plt.plot(x, (2*n*x**2)/(1 + (n**2)*x**4), 'g', label='n='+str(n))
n = 4
plt.plot(x, (2*n*x**2)/(1 + (n**2)*x**4), 'y', label='n='+str(n))

plt.legend(loc='upper right')

# show the plot
plt.show()