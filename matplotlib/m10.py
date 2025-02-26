import numpy as np
import matplotlib.pyplot as plt
# Create data
g1 = np.array( [ [89, 90, 70, 89, 100, 80, 90, 100, 80, 34],
 [1,2,3,4,5,6,7,8,9,10]] )
g2 = np.array([ [30, 29, 49, 48, 100, 48, 38, 45, 20, 30],  
 [1,2,3,4,5,6,7,8,9,10]])
g3 = np.array([ [ 69, 90, 70, 59, 70, 80, 40, 80, 55, 24],
 [1,2,3,4,5,6,7,8,9,10]])
# Create plot
x, y = g1
plt.scatter(y, x, alpha=0.8, c='red', edgecolors='none', s=30, label='Red House')
x, y = g2
plt.scatter(y, x, alpha=0.8, c='green', edgecolors='none', s=30, label='Green House')
x, y = g3
plt.scatter(y, x, alpha=0.8, c='blue', edgecolors='none', s=30, label='Blue House')

# plt.legend(loc=2)
plt.xlabel('Number of observations ')
plt.ylabel('Number of observations')
plt.show()