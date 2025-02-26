import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3])

y = np.array([3,8,1,10])
plt.subplot(2,1,1)
plt.plot(x,y)

# plot 2

x2 = np.array([0,1,2,3])
y2 = np.array([10,20,30,40])
plt.subplot(2,1,2)
plt.plot(x2,y2,'r-')

plt.show()