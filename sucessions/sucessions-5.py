import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(0, 2*np.pi, 100)
# setting the axes at the centre
fig = plt.figure()

# n(cosx)^nsenx
# plot the functions
n = 1
plt.plot(x, n*(np.cos(x)**n)*np.sin(x), 'b', label='n='+str(n))
n=2
plt.plot(x, n*(np.cos(x)**n)*np.sin(x), 'r', label='n='+str(n))
n=3
plt.plot(x, n*(np.cos(x)**n)*np.sin(x), 'g', label='n='+str(n))
n=4
plt.plot(x, n*(np.cos(x)**n)*np.sin(x), 'y', label='n='+str(n))
plt.legend(loc='upper right')

# show the plot
plt.savefig("ejercicio-5.png")
plt.show()