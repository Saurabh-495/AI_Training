import numpy as np
import matplotlib.pyplot as plt

names = ['group a' , 'group b' , 'group c']
value = [1,10,100]
plt.figure(figsize=(9,3))

plt.subplot(131)

plt.bar(names, value)

plt.subplot(132)

plt.scatter(names, value)

plt.subplot(133)

plt.plot(names, value,"r--")
plt.legend()

plt.suptitle('Categorical Plotting')

plt.show()