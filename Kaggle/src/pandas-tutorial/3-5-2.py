import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(-5,5)
y = x**5 - 12*x

plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)

plt.savefig('3-5-2.png')

